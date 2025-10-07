import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://automationexercise.com/", wait_until="domcontentloaded")
    assert "https://automationexercise.com" in page.url
    print(page.title())

    page.get_by_text("Signup / Login").click()
    page.wait_for_selector('input[type="text"]').fill("test user")
    page.wait_for_selector('input[data-qa="signup-email"]').fill("test88992289@yopmail.com")
    page.get_by_role("button", name="Signup").click()
    assert "https://automationexercise.com/signup" in page.url
    print("signup page loaded")
    page.wait_for_selector("#id_gender2").click()
    page.wait_for_selector("#password").fill("Test@123")
    page.locator("#days").click()
    page.select_option("#days", value="22")
    page.locator("#months").click()
    page.select_option("#months", label="June")
    page.locator("#years").click()
    page.select_option("#years", index=10)
    page.locator("#newsletter").click()
    page.locator("#optin").click()
    page.locator("#first_name").fill("Test")
    page.locator("#last_name").fill("user")
    page.locator("#company").fill("Microsoft")
    page.locator("#address1").fill("Delhi")
    page.locator("#state").fill("delhi")
    page.locator("#city").fill("delhi")
    page.locator("#zipcode").fill("110064")
    page.locator("#mobile_number").fill("7667675757")
    page.get_by_text("Create Account").click()
    page.wait_for_url("https://automationexercise.com/account_created")
    text=page.locator("h2[data-qa='account-created']").inner_text()
    print(text)
    page.wait_for_selector('a[data-qa="continue-button"]').click()
    assert "https://automationexercise.com/" in page.url
    page.wait_for_selector('a[href="/delete_account"]').click()
    print(page.locator('h2[data-qa="account-deleted"]').inner_text())

