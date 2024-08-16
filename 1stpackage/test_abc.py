import pytest


@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")
    print(order)


    # Assert
    assert order == ["a", "b"]

