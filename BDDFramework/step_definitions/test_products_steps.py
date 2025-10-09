from operator import index

from pytest_bdd import scenarios, given, when, then

from ..Pages.Login import LoginPage

scenarios("../features/products.feature")

@given('the user logs in with "newtest231@yopmail.com" and "Test@123"')
def user_logs_in(page, login_obj):
    login_obj.page_navigation(page) # navigates to login url
    login_obj.validLogin("newtest231@yopmail.com", "Test@123")

@when('the user clicks on the "Products" link')
def productClick(page, product_obj):
    product_obj.clickingOnProducts()


@then('the user should be navigated to the products page')
def reached_to_products(page, product_obj):
    assert "https://automationexercise.com/products" in page.url
    print("products loaded")


@then('the page should display a company logo')
def logo_display(page, product_obj):
    product_obj.logoVisibilty()

@then('the page should display a list of products')
def product_list(page, product_obj):
    assert product_obj.is_product_list_displayed() # is_visible will return T or F
    print("product list displayed")

@then('the page should display a count of products')
def product_count(page, product_obj):
    product_obj.count_of_products()

@given('products are visible')
def product_loaded(page, product_obj):
    product_obj.navigate_to_products()

@when('the user clicks on “View Product” for a product')
def view_click(page, product_obj):
    product_obj.clicking_on_view()

@then('the user should be on a product detail page')
def verify_view_url(page):
    assert "https://automationexercise.com/product_details/1" in page.url
    print("product view is available")

@given('the product list is visible')
def prdocut_list(page, product_obj):
    product_obj.navigate_to_products()


@when('the user hovers over a product and clicks "Add to cart"')
def clicking_on_add_to_cart(page, product_obj):
    product_obj.clicking_addToCart()

@then('a modal “Added!” or confirmation should appear')
def model(page, product_obj):
    text=product_obj.model_displayed()
    assert "Your product has been added to cart" in text

@then('the user can click on “Continue Shopping”')
def continueShoppingClick(product_obj):
    product_obj.clicking_on_continue_shopping()
    print("continue shopping clicked")

@given('the user is on the All Products page')
def product_page(page, product_obj):
    product_obj.navigate_to_products()

@when('the user enters “top” in the product search box and clicks “Search”')
def serchingProduct(page, product_obj):
    product_obj.typingOnSearch()
    print("top searched")

@then('the “SEARCHED PRODUCTS” section should be shown')
def searchedHeader(page, product_obj):
    header_text=product_obj.gettingHeaderText()
    print("header text is:", header_text)

@then('every displayed product in results should match or contain “top”')
def matchedResults(page, product_obj):
    products=product_obj.getMatchedProducts()
    matched = [p for p in products if "top" in p.lower()]
    print(f"Total searched products containing 'top': {len(matched)}")

@given('the product list is visible')
def product_page(page, product_obj):
    product_obj.navigate_to_products()

@when('the user adds 4 products via Add to cart')
def addProducts(product_obj):
    product_obj.addMultipleProducts()

@when('clicks Cart button')
def cartClick(page, product_obj):
    product_obj.clicking_on_cart(page)
    print("cart page loaded")

@then('the cart page should list those products')
def cartList(page, product_obj):
    product_obj.getting_cart_items()

@given('I am on the Products page')
def product_page2(page, product_obj):
    product_obj.navigate_to_products()

@when('I click on the "WOMEN" category link & click on the "DRESS" sub-category link')
def categoryClicked(page, product_obj):
    product_obj.clickinOnCategory()
    print("women category & Dress subcategory clicked")


@then('the page URL should contain "/category_products/1"')
def validateUrl(page):
    assert "https://automationexercise.com/category_products/1" in page.url
    print("Dress sub category page loaded")

@then('I should see a heading with text "WOMEN - DRESS PRODUCTS"')
def validateHeaderText(page, product_obj):
    text=product_obj.headerText()
    print("Header text is :", text)

@then('I should see only products belonging to the "WOMEN - DRESS" category')
def getResult(page, product_obj):
    names=product_obj.dressResult()
    assert len(names)>0, "No products found for this category"
    for n in names:
        assert "dress" in n.lower()
        print("Product list with Dress :", names)






























