import logging
from playwright.sync_api import Page

logger  = logging.getLogger('foo')

class BasePage:
    URL: str
    BaseUrl : str

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)
        logger.info(f"Navigate to URL '{self.URL}'")