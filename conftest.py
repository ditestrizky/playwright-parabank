import os
import pytest
from pages.login_page import LoginPage
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture
def logged_in_page(page):
    username = os.getenv("PB_USER")
    password = os.getenv("PB_PASS")

    if not username or not password:
        pytest.fail("Environment variables PB_USER and PB_PASS must be set for this test. see .env.example for reference")

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(username, password)
    yield page