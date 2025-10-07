import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp", wait_until="domcontentloaded")
    page.locator("label:has-text('One') >> input[type='checkbox']").check()
    page.locator("label:has-text('Two') >> input[type='checkbox']").check()
    print("both checked")

    page.locator("label:has-text('One') >> input[type='checkbox']").uncheck()
    time.sleep(3000)
    page.locator("label:has-text('Two') >> input[type='checkbox']").uncheck()
    print("both unchecked")

    checkboxes = page.locator("input[type='checkbox']").all()
    for cb in checkboxes:
        cb.check()
time.sleep(3000)

