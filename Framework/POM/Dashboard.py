from Framework.POM.OrderHistory import OrderHistory


class Dashboard:
    def __init__(self, page):
        self.page=page

    def OrderClick(self):
        self.page.get_by_role("button", name="ORDERS").click()
        historyPage_obj=OrderHistory(self.page)
        return historyPage_obj


