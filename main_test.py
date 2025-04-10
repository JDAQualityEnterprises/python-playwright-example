import pytest
import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pytest_check import check

from models.HomeLinks import HomeLinks

def test_home_has_title(page: Page, pytestconfig: pytest.Config) -> None:
    home_page = HomePage(page, pytestconfig.getini('base_url'))

    expect(home_page.page).to_have_title(re.compile("JDA Quality Enterprises Limited"))

def test_home_has_links(page: Page, pytestconfig: pytest.Config) -> None:
    home_page = HomePage(page, pytestconfig.getini('base_url'))

    # Required until python plyawright expect has soft assertions
    with check:
        expect(home_page.home_link).to_have_text(re.compile(HomeLinks.Home))
    with check:
        expect(home_page.contact_link).to_have_text(re.compile(HomeLinks.Contact))
    with check:
        expect(home_page.aboutus_link).to_have_text(HomeLinks.AboutUs)
    with check:
        expect(home_page.clients_link).to_have_text(HomeLinks.Clients)
    with check:
        expect(home_page.email_links).to_have_count(1)