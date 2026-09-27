import pytest
import json
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from utils.json_utils import load_json
from utils.session_storage import (
    save_session_storage_to_file,
    restore_session_storage_from_file,
    get_session_storage
)

# Load data-driven inputs
login_datasets = load_json("testdata/login_data.json")

@pytest.mark.smoke
@pytest.mark.parametrize("data", login_datasets)
def test_login_scenarios(page, data, logger):
    """1 & 2. Valid/Invalid Login & Error Validation (Data-driven)."""
    logger.info(f"Executing login test for user: {data['username']}")
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(data["username"], data["password"])

    if data["should_succeed"]:
        page.wait_for_url("**/inventory.html")
        assert "inventory.html" in page.url
    else:
        error_msg = login_page.get_error_message()
        assert data["expected_error"] in error_msg

@pytest.mark.readonly
def test_verify_products_displayed(logged_in_page, logger):
    """3. Verify products are displayed."""
    logger.info("Verifying product list display.")
    products_page = ProductsPage(logged_in_page)
    items = products_page.get_product_names()
    assert len(items) > 0
    assert "Sauce Labs Backpack" in items

@pytest.mark.regression
def test_add_product_to_cart(logged_in_page, logger):
    """4. Add product to cart and validate cart count."""
    logger.info("Adding item to cart.")
    products_page = ProductsPage(logged_in_page)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    assert products_page.get_cart_count() == 1

@pytest.mark.regression
def test_remove_product_from_cart(logged_in_page, logger):
    """5. Remove product from cart."""
    logger.info("Adding and removing item from cart.")
    products_page = ProductsPage(logged_in_page)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    assert products_page.get_cart_count() == 1
    products_page.remove_product_from_cart("Sauce Labs Backpack")
    assert products_page.get_cart_count() == 0

@pytest.mark.readonly
def test_verify_product_details(logged_in_page):
    """6. Verify product details page navigation."""
    products_page = ProductsPage(logged_in_page)
    products_page.click_product_name("Sauce Labs Backpack")
    logged_in_page.wait_for_url("**/inventory-item.html?id=*")
    assert "inventory-item.html" in logged_in_page.url

@pytest.mark.readonly
def test_sort_products(logged_in_page):
    """7. Sort products Name Z-A."""
    products_page = ProductsPage(logged_in_page)
    products_page.sort_products_by("za")
    names = products_page.get_product_names()
    assert names == sorted(names, reverse=True)

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_flow(logged_in_page, logger):
    """8. Complete checkout and validate successful order."""
    logger.info("Starting complete checkout scenario.")
    reg_data = load_json("testdata/registration_data.json")
    products_page = ProductsPage(logged_in_page)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.proceed_to_checkout()
    checkout_page.fill_information(
        reg_data["firstName"], reg_data["lastName"], reg_data["postalCode"]
    )
    checkout_page.finish_checkout()
    
    msg = checkout_page.get_completion_message()
    assert msg == "Thank you for your order!"

@pytest.mark.regression
def test_session_storage_operations(logged_in_page, logger):
    """Session storage read, write, save, clear, and restore."""
    logger.info("Executing session storage read/write/restore test.")
    
    # Save active session storage to JSON
    save_session_storage_to_file(logged_in_page, "testdata/session_data.json")
    original_data = get_session_storage(logged_in_page)
    assert len(original_data) >= 0

    # Clear and restore
    logged_in_page.evaluate("sessionStorage.clear()")
    assert len(get_session_storage(logged_in_page)) == 0

    restore_session_storage_from_file(logged_in_page, "testdata/session_data.json")
    restored_data = get_session_storage(logged_in_page)
    assert restored_data == original_data