import pytest


#@pytest.fixture(scope="class")
@pytest.fixture
def setup():
    print("use fixture")
    yield
    print("use yield")