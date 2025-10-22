import pytest

from .Pages.Cart import CartPage
from .Pages.Login import LoginPage
from .Pages.products import Products


@pytest.fixture
def login_obj(page):
    return LoginPage(page)   # ✅ creates a reusable Login object

@pytest.fixture
def product_obj(page):
    return Products(page)

@pytest.fixture
def cart_obj(page):
    return CartPage(page)
