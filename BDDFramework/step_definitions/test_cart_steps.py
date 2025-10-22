from operator import index

from pytest_playwright.pytest_playwright import page

from ..Pages.Login import LoginPage
from pytest_bdd import scenarios, given, when, then
from BDDFramework.step_definitions import test_login_steps
from BDDFramework.step_definitions import test_products_steps

from ..Pages.products import Products
from ..Pages.Cart import CartPage
scenarios("../features/cart.feature")


@given('user is logged in with valid credentials')
def login(page, login_obj):
    login_obj.page_navigation(page)
    login_obj.validLogin("newtest231@yopmail.com", "Test@123")
    page.wait_for_url("https://automationexercise.com/", timeout=70000)
    print("logged in success")

@given('user has added products to cart')
def addProducts(product_obj):
    product_obj.addMultipleProducts()

@when('user click on cart button')
def cartClick(product_obj):
    product_obj.clicking_on_cart()

@then('all added products should be listed in the cart')
def getProductCount(cart_obj):
    count=cart_obj.productCount()
    print(f"total {count} products added")

@then('each product should display correct name, price, quantity, and total')
def productListOnCart(cart_obj):
    values=cart_obj.getCartTable()
    print(values, end=",")