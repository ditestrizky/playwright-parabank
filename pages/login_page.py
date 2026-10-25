from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    path = "/parabank/index.htm"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_button = page.get_by_role("button", name="Log In")
        self.logout_button = page.get_by_role("link", name="Log Out")
        self.err_message = page.locator("p.error")

    def login(self, username: str, password:str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()