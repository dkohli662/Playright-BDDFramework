from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page=page
        self.email='input[data-qa="login-email"]'
        self.password='input[data-qa="login-password"]'
        self.submit='button[data-qa="login-button"]'
        self.error_message = page.locator("p:has-text('Your email or password is incorrect!')")

    def page_navigation(self, page):
        page.goto("https://automationexercise.com/login", wait_until="domcontentloaded")

    def validLogin(self, username, password):
        self.page.fill(self.email, username)
        self.page.fill(self.password, password)
        self.page.click(self.submit)
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")
        print("logged in success")




