from playwright.sync_api import Page
from pages.base_page import BasePage
from models.HomeLinks import HomeLinks


class HomePage(BasePage):
    URL = "/"

    def __init__(self, page: Page, url: str = "/") -> None:
        super().__init__(page)
        displayed_list = page.get_by_role("list", include_hidden=False)

        self.home_link = displayed_list.get_by_role("link",name="Home")
        self.contact_link = displayed_list.get_by_role("link",name="Contact")
        self.aboutus_link = displayed_list.get_by_role("link",name="About Us")
        self.clients_link = displayed_list.get_by_role("link",name="Clients")

        self.email_links = page.get_by_text(HomeLinks.Email)
        self.URL = url

        self.load()