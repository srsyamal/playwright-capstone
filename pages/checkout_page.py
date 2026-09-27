from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.locator("[data-test='checkout']")
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = page.locator("[data-test='continue']")
        self.finish_btn = page.locator("[data-test='finish']")
        self.complete_header = page.locator(".complete-header")

    def proceed_to_checkout(self):
        self.checkout_btn.click()

    def fill_information(self, fname: str, lname: str, zip_code: str):
        self.first_name.fill(fname)
        self.last_name.fill(lname)
        self.postal_code.fill(zip_code)
        self.continue_btn.click()

    def finish_checkout(self):
        self.finish_btn.click()

    def get_completion_message(self) -> str:
        self.complete_header.wait_for(state="visible")
        return self.complete_header.inner_text()