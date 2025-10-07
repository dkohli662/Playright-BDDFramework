import pytest


@pytest.fixture(scope="session")
def creds(request): # request is global parameter which can be use to access parameters
    return request.param