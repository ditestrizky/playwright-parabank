import uuid
import pytest
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage

def test_register_valid(page: Page):
    unique_username = f"haryadi_{uuid.uuid4().hex[:4]}"
    register_page = RegisterPage(page)

    register_page.goto()
    register_page.fill_valid_form(unique_username)
    register_page.submit()

    expect(register_page.welcome_heading).to_have_text(f"Welcome {unique_username}")

    #Opsi Lain: to_contain_text("Welcome") -> cukup untuk cek sebagian teks saja, tidak harus sama persis
    #expect(page.locator("#rightPanel h1")).to_contain_text("Welcome")

@pytest.mark.parametrize("field_name",[
    "customer.firstName",
    "customer.lastName",
    "customer.address.city",
    "customer.username",
])
def test_register_required_field(page: Page,field_name):
    unique_username=f"haryadi_{uuid.uuid4().hex[:4]}"
    register_page = RegisterPage(page)

    register_page.goto()
    register_page.fill_valid_form(unique_username)
    page.locator(f"input[name='{field_name}']").fill("")

    register_page.submit()

    expect(register_page.error_for(field_name)).to_contain_text("is required")