from playwright.sync_api import Page


class CartPage:

    def __init__(self, page:Page):
        self.page=page
        self.proceed_to_pay_btn = page.locator("a.btn.btn-default.check_out")
        self.rows= page.locator("#cart_info_table tbody tr")



    def productCount(self):
        return self.rows.count()

    def getCartTable(self):
        table_data=[]

        for i in range(self.rows.count()):
            row=self.rows.nth(i)

            product_name = row.locator(".cart_description h4 a").inner_text()
            brand = row.locator(".cart_description p").inner_text()
            price = row.locator(".cart_price p").inner_text()
            quantity = row.locator(".cart_quantity button").inner_text()
            total = row.locator(".cart_total p").inner_text()

            table_data.append({"Product name" : product_name, "Brand" : brand, "Price" : price, "Quantity" : quantity, "Total" : total})
            return table_data


    def removeItem(self):
        if self.rows.count() == 0:
            raise Exception("Cart is empty, no product to delete!")

        first_row = self.rows.nth(0)
        delete_button = first_row.locator("a.cart_quantity_delete")
        delete_button.click()
        self.page.wait_for_timeout(2000)
        print("First row deleted")












