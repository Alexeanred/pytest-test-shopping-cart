import pytest
from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock

@pytest.fixture
def cart():
    return ShoppingCart(2)
def test_can_add_item_to_shopping_cart(cart):
    cart.add("quan jean")
    assert cart.size() == 1

def test_when_item_added_shopping_cart_contains_item(cart):
    cart.add("quan jean")
    assert 'quan jean' in cart.get_items() 

def test_when_added_more_than_max_items_test_fails(cart):
    for _ in range(2):
        cart.add("quan jean")
    with pytest.raises(OverflowError):
        cart.add("quan jean")

def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0



