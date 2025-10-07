import pytest
from playwright.sync_api import Playwright

from DataDrivenFramework.Utils import config
from DataDrivenFramework.pages.Dahboard import Dashboard


@pytest.fixture(scope="session")
def creds():
    """Load all credentials (valid + invalid) from creds.json"""
    return config.load_credentials()

@pytest.fixture(scope="session")
def valid_creds(creds):
    """Return only valid user credentials"""
    return creds["valid_user"]

@pytest.fixture(scope="session")
def invalid_creds(creds):
    """Return only invalid user credentials"""
    return creds["invalid_user"]

@pytest.fixture(scope="session")
def logged_in_context(playwright: Playwright, valid_creds):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # login only once
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(valid_creds["username"])
    page.locator("#userPassword").fill(valid_creds["password"])
    page.locator("#login").click()
    page.wait_for_url("https://rahulshettyacademy.com/client/#/dashboard/dash")


    yield context   # provide to all tests

    context.close()
    browser.close()
@pytest.fixture
def cart_ready_page(logged_in_context):
    page = logged_in_context.new_page()

    # go to dashboard
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    dash = Dashboard(page)

    # add item to cart
    count=dash.addCart()

    # navigate to cart page
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/cart")
    return page


