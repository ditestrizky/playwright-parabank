import os
import pytest
from pages.login_page import LoginPage
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(os.environ["PB_USER"],os.environ["PB_PASS"])
    yield page