import pytest
import products


# TODO: improve tests
def test_create_product():
    product = products.Product("Test Product", 10, 50)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 50
    assert product.is_active()


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        products.Product("", -10, 0)


def test_product_quantity_decreases_on_purchase():
    product = products.Product("Test Product", 10, 50)
    product.buy(30)
    assert product.quantity == 20


def test_product_becomes_inactive_at_zero_quantity():
    product = products.Product("Test Product", 10, 10)
    product.buy(10)
    assert not product.is_active()


def test_product_purchase_returns_correct_output():
    product = products.Product("Test Product", 10, 10)
    purchase_price = product.buy(5)
    assert purchase_price == 50.0


def test_product_purchase_with_large_quantity_raises_exception():
    product = products.Product("Test Product", 10, 10)
    assert product.buy(15) == 0.0


pytest.main()
