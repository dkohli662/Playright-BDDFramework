from playwright.sync_api import Page


def test_childWindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    with page.expect_popup() as newPage:
        page.locator(".blinkingText").click()
        childPage=newPage.value
        text=childPage.locator(".red").text_content()
        print(text) # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        text2 = text.split("at")# o index-Please email us & on 1 index- mentor@rahulshettyacademy.com with below template to receive response
        email=text2[1].strip().split(" ")[0] # 0 index-mentor@rahulshettyacademy.com
        assert email=="mentor@rahulshettyacademy.com"

