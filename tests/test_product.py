from src.product import Product


def test_product_initializations():
    product = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой ноутбук"
    assert product.price == 999.99
    assert product.quantity == 10
