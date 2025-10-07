import time

from playwright.sync_api import Page # importing page class of playwright package

def test_firstCode(playwright): # playright is a global fixture
    browser=playwright.chromium.launch(headless=False) # will start browser engine
    context=browser.new_context() # will start new browser incognito without any cache cookie stored
    page=context.new_page() # will open up browser tab that is a browser page
    page.goto("https://chatgpt.com/") # will hit this url on browser

    # shortcut way to define above 3 lines in a single line

def test_shortCut(page:Page): # page is a fixture defined in  Page class of playwright package
    page.goto("https://chatgpt.com")

def test_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option(value="teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)



