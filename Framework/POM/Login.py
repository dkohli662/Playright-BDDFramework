from Framework.POM.Dashboard import Dashboard
from Framework.POM.OrderHistory import OrderHistory


class Login:
    def __init__(self, page):
        self.page=page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="login").click()

        # creating obj of dashboard page

        dashboard_obj=Dashboard(self.page)
        return dashboard_obj







