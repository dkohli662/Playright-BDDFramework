import pytest


@pytest.fixture(scope="module")
def preWork():
    print("first setup")
    return "Pass"