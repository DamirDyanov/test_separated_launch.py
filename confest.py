import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture()
def run():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()
        return page

