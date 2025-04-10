from playwright.sync_api import Page
from pages.base_page import BasePage


class ContactsPage(BasePage):
    URL = "/"

    def __init__(self, page: Page, url: str = "/") -> None:
        super().__init__(page)
        self.URL = url
        self.contact_link = "contact"
        self.heading = page.get_by_role("heading", level=1)