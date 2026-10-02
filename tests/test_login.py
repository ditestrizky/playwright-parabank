import os
import re
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_valid(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("john","passwor1d")
    expect(page).to_have_url(re.compile("overview"))
    expect(login_page.logout_button).to_be_visible()
    

def test_login_empty_password(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("john","")

    expect(login_page.err_message).to_have_text(
        "Please enter a username and password."
    )