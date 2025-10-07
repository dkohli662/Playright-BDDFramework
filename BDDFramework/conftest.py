import pytest

from .Pages.Login import LoginPage
from .Pages.products import Products


@pytest.fixture
def login_obj(page):
    return LoginPage(page)   # ✅ creates a reusable Login object

@pytest.fixture
def product_obj(page):
    return Products(page)
