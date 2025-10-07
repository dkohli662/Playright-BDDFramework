import time

from playwright.sync_api import Playwright


def test_firefox(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    page=browser.new_page()
    time.sleep(5)

