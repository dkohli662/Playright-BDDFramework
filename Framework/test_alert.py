import time

from playwright.sync_api import Page, expect


# print message of alert and clickin on OK
def test_alert(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: (print("Alert text:", dialog.message), dialog.accept()))
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

# clicking on cancel of alert

def test_alert2(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog : dialog.dismiss()) # clicking on cancel of alert box
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

# handeling frames

def test_frame(page:Page):
    pageFrame=page.frame_locator("#courses-iframe") # fidning frame in paent html page.
    pageFrame.get_by_role("link", name="All Access plan").wait_for()
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")

# mouse hover

def test_hover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    items=page.locator(".mouse-hover-content") # finding sub menu box by class name.
    c=items.count()
    print(f"Total menu items : {c}")
    for i in range(c):
        print(items.nth(i).inner_text()) # inner text is use to retrive text of submenu items.

# print specic item of submenu
    page.get_by_role("link", name="Reload").click()
    print("page gets reload")

