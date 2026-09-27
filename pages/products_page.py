from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.cart_link = page.locator(".shopping_cart_link")

    def get_title(self) -> str:
        return self.title.inner_text()

    def get_product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def add_product_to_cart(self, product_name: str):
        item = self.inventory_items.filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart(self, product_name: str):
        item = self.inventory_items.filter(has_text=product_name)
        item.get_by_role("button", name="Remove").click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def sort_products_by(self, option_value: str):
        # option_value e.g., 'az', 'za', 'lohi', 'hilo'
        self.sort_dropdown.select_option(option_value)

    def open_cart(self):
        self.cart_link.click()

    def click_product_name(self, product_name: str):
        self.page.get_by_text(product_name).click()