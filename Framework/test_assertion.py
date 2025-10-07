# assertion to check error message
from playwright.sync_api import Page, expect


def test_assertion(page:Page):
    page.goto("https://chatgpt.com")
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("dkohli")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
