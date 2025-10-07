import time

from playwright.sync_api import Page, expect


def test_UIValidation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    print("page gets loaded")
    item1=page.locator("app-card").filter(has_text="Nokia Edge")
    item1.get_by_role("button").click()
    item2 = page.locator("app-card").filter(has_text="iphone X")
    item2.get_by_role("button").click()
    page.get_by_text("checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    print("test case passed")
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Nokia Edge")).to_be_visible()
    print("both items found in the list")
    page.get_by_text("Checkout").click()
    page.locator("#country").fill("Delhi, India 110044")
    #page.locator("#checkbox2").click()
    page.get_by_role("button", name="Purchase").click()
    expect(page.get_by_text("Success! Thank you! Your order will be delivered in next few weeks :-)."))
    time.sleep(5)




