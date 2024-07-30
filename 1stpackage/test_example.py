import pytest


@pytest.mark.usefixtures("setup")
class test_fixture:
    def test_mag(self):
        print("test1-------")

    def test_add(self):
        print("test2---")


@pytest.fixture
def setup():
    print("use fixture")
    yield
    print("use yield")
#@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
#def test_multiplication_11(num, output):
   #assert 11*num == output