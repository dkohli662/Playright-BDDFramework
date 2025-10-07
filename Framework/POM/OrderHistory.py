from Framework.POM.OrderDetails import OrderDetails


class OrderHistory:
    def __init__(self, page):
        self.page=page

    def OderHistory(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)  # finding row that matched with orderId found by API call
        row.get_by_role("button", name="View").click()
        detailPage_obj=OrderDetails(self.page)
        return detailPage_obj

