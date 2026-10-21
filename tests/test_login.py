import os
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_valid(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(os.environ["PB_USER"],os.environ["PB_PASS"])
    expect(page).to_have_url(re.compile("overview"))
    expect(login_page.logout_button).to_be_visible()
    
def test_login_empty_password(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("john","")

    expect(login_page.err_message).to_have_text(
        "Please enter a username and password."
    )

def test_logout(logged_in_page):
    login_page = LoginPage(logged_in_page)
    login_page.logout()

    expect(login_page.login_button).to_be_visible()
    expect(login_page.logout_button).to_be_hidden()

