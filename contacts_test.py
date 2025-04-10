import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.contacts_page import ContactsPage


def test_contact_page_has_title(page: Page, pytestconfig: pytest.Config) -> None:

    home_page = HomePage(page, pytestconfig.getini('base_url'))

    home_page.contact_link.click()

    contacts_page = ContactsPage(page)

    expect(contacts_page.heading).to_have_text("Contact")