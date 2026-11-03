import os
import pytest
from pages.login_page import LoginPage
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope="session")
def credentials():
    username = os.getenv("PB_USER")
    password = os.getenv("PB_PASS")

    if not username or not password:
        pytest.fail("Environment variables PB_USER and PB_PASS must be set for this test. See .env.example for reference")
    return (username,password)

@pytest.fixture
def logged_in_page(page,credentials):
    username, password = credentials

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(username, password)
    yield page