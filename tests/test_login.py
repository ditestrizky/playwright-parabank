import os
import re
from playwright.sync_api import Page, expect

def test_login_valid(page: Page):
    page.goto("https://parabank.parasoft.com")
    page.locator("input[name='username']").fill(os.environ["PB_USER"])
    page.locator("input[name='password']").fill(os.environ["PB_PASS"])
    page.get_by_role("button", name="Log In").click()

    expect(page).to_have_url(re.compile("overview"))
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

def test_login_invalid(page: Page):
    page.goto("https://parabank.parasoft.com")
    page.locator("input[name='username']").fill("john")
    page.locator("input[name='password']").fill("qwerty123")
    page.get_by_role("button", name="Log In").click()

    expect(page.locator("p.error")).to_have_text(
        "The username and password could not be verified."
    )