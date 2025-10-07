from playwright.sync_api import expect


class OrderDetails:
    def __init__(self, page):
        self.page=page

    def getMessaeg(self, orderId):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
        print("reached to thank you page and our order id is :", orderId)
