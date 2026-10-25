from playwright.sync_api import Page

class BasePage:
    path = None

    def __init__(self, page: Page):
        self.page = page
        self.right_panel = page.locator("div#rightPanel")

    def goto(self):
        if self.path is None:
            raise NotImplementedError(
                f"{type(self).__name__} belum mengisi 'path'"
            )
        self.page.goto(self.path)
