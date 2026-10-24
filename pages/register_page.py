from playwright.sync_api import Page
from pages.base_page import BasePage

class RegisterPage(BasePage):
    path = "/parabank/register.htm"

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.locator("#customer\\.firstName")
        self.last_name = page.locator("#customer\\.lastName")
        self.street = page.locator("#customer\\.address\\.street")
        self.city = page.locator("#customer\\.address\\.city")
        self.state = page.locator("#customer\\.address\\.state")
        self.zip_code = page.locator("#customer\\.address\\.zipCode")
        self.phone = page.locator("#customer\\.phoneNumber")
        self.ssn = page.locator("#customer\\.ssn")
        self.username = page.locator("#customer\\.username")
        self.password = page.locator("#customer\\.password")
        self.confirm_password = page.locator("#repeatedPassword")
        self.register_button = page.get_by_role("button", name="Register")
        self.welcome_heading = self.right_panel.locator("h1")
    
    def fill_valid_form(self, unique_username:str):
        self.first_name.fill("Haryadi")
        self.last_name.fill("hartanto")
        self.street.fill("semeru")
        self.city.fill("grogol")
        self.state.fill("jakarta barat")
        self.zip_code.fill("11450")
        self.phone.fill("6285174418299")
        self.ssn.fill("12321123")
        self.username.fill(unique_username)
        self.password.fill("qwerty123")
        self.confirm_password.fill("qwerty123")

    def submit(self):
        self.register_button.click()

    def error_for(self, field_name: str):
        return self.page.locator(f"span[id='{field_name}.errors']")