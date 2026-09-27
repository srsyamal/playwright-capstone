import pytest
from playwright.sync_api import Playwright, APIRequestContext
from utils.logger import setup_logger

@pytest.fixture(scope="session")
def logger():
    return setup_logger("capstone_logger")

@pytest.fixture(scope="function")
def logged_in_page(page, logger):
    """Fixture with setup and teardown using yield."""
    logger.info("Setup: Navigating to SauceDemo and logging in")
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/inventory.html")
    
    yield page
    
    logger.info("Teardown: Clearing session and navigating away")
    page.evaluate("sessionStorage.clear()")

@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()