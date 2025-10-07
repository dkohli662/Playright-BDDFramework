from playwright.sync_api import Page, Playwright, expect

from utils.ApiUtils import API

# login from UI creating an order from API & validating order id from order history in UI


def test_e2e(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()

# Create an order -> order ID from API

    obj = API()  # creating an obj of class API
    orderId=obj.createOrder(playwright)  # calling method of class API

# login

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("dkohli@ex2india.com")
    page.get_by_placeholder("enter your passsword").fill("Test@123")
    page.get_by_role("button", name="login").click()
# go to order history page & check this order id is present or not

    page.get_by_role("button", name="ORDERS").click()
    row=page.locator("tr").filter(has_text=orderId) # finding row that matched with orderId found by API call
    row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print("reached to thank you page and our order id is :",orderId )
    context.close()
















