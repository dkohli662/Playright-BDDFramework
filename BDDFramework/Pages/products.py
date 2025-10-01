from itertools import count

from playwright.sync_api import Page


class Products:
    def __init__(self, page:Page):
        self.page=page
        self.products_button = 'a[href="/products"]'
        self.search_bar=page.locator('input[name="search"]')
        self.search_button=page.locator("#submit_search")
        self.logo=page.locator('img[alt="Website for practice"]')
        self.product_list=page.locator("div.product-image-wrapper")
        self.view_button=page.locator("a:has-text('View Product')")
        self.add_to_cart_button=page.locator("a[data-product-id]") # total 68
        self.model=page.locator("div.modal-content")
        self.continue_btn=page.locator("button:has-text('Continue Shopping')")
        self.cart_btn=page.locator("a[href='/view_cart']").first
        self.cart_items=page.locator("#cart_info_table tbody tr")

    def navigate_to_products(self):
        if "/products" not in self.page.url:
            self.page.goto("https://automationexercise.com/products",wait_until="domcontentloaded",timeout=60000)

    def clickingOnProducts(self):
        self.page.click(self.products_button)
        self.page.goto("https://automationexercise.com/products", wait_until="domcontentloaded")

    def logoVisibilty(self):
        if self.logo.is_visible():
            print("logo gets visible")
        else:
            print("logo is not visible")

    def is_product_list_displayed(self):
        try:
            # wait up to 10s for the first product to become visible
            self.product_list.first.wait_for(state="visible", timeout=10000)
            return self.product_list.first.is_visible()
        except Exception:
            return False


    def count_of_products(self):
        product_count=self.product_list.count()
        print("total products are :", product_count)

    def clicking_on_view(self):
        self.view_button.first.click()

    def clicking_addToCart(self):
        first_element=self.add_to_cart_button.first
        first_element.hover()
        first_element.click()
        self.model.wait_for(state="visible", timeout=5000)
        print("model opened")


    def model_displayed(self):
            model_text=self.model.text_content()
            return model_text
    def clicking_on_continue_shopping(self):
        self.page.locator("button:has-text('Continue Shopping')").click()

    def typingOnSearch(self):
        self.search_bar.click()
        self.search_bar.fill("top")
        self.search_button.click()
        self.page.wait_for_url("https://automationexercise.com/products?search=top")

    def gettingHeaderText(self):
        return self.page.locator("h2:has-text('Searched Products')").inner_text()

    def getMatchedProducts(self):
        searched_items=self.page.locator("div.features_items .productinfo")
        print("Total items are:", searched_items.count())
        prodcut_names=[searched_items.nth(i).text_content().strip() for i in range(searched_items.count())]
        return prodcut_names

    def addMultipleProducts(self):
        count=4
        for index in range(count):
            product = self.product_list.nth(index)
            product.hover()
            add_to_cart = product.locator(".overlay-content a[data-product-id]") # will find into that prodcut card
            add_to_cart.wait_for(state="visible")  # optional, already mostly handled by click
            add_to_cart.click()
            self.page.wait_for_selector("#cartModal", state="visible", timeout=5000)

            self.continue_btn.click()
            self.page.wait_for_selector("#cartModal", state="hidden", timeout=5000)
            print(f"Product {index} added successfully")

    def clicking_on_cart(self, page):
        #if "/products" not in self.page.url:
            #self.page.goto("https://automationexercise.com/products",wait_until="domcontentloaded",timeout=60000)

        self.cart_btn.click()
        page.wait_for_url("https://automationexercise.com/view_cart")  # waits until URL matches

    def getting_cart_items(self):
        cart_count = self.cart_items.count()
        print("total items in cart :", cart_count)


        for i in range(cart_count):
            item_text = self.cart_items.nth(i).inner_text().strip()
            print(f"item at {i} is {item_text}")


















