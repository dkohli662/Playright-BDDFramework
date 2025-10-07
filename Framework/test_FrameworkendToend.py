import json

import pytest
from playwright.sync_api import Page, Playwright, expect

from utils.ApiUtils import API


# json file->util->access into test
with open('Data/credentials.json') as f:
    test_data = json.load(f)  # will change json into python obj stored in test_data
    list = test_data['user_credentials']  # will return list of item in form of ind, value

@pytest.mark.parametrize('creds' , list) # creds is any var name that will hold paramtr values
def test_e2e(playwright:Playwright, creds): # user_creds is my fixture define in conftext
    browser=playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()

    obj = API()  # creating an obj of class API
    orderId = obj.createOrder(playwright, creds)  # calling method of class API
# login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(creds["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(creds["userPassword"])
    page.get_by_role("button", name="login").click()
# go to order history page & check this order id is present or not

    page.get_by_role("button", name="ORDERS").click()
    row=page.locator("tr").filter(has_text=orderId) # finding row that matched with orderId found by API call
    row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print("reached to thank you page and our order id is :",orderId )
    context.close()
















