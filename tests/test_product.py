from src.product import Product


def test_product_initializations():
    product = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой ноутбук"
    assert product.price == 999.99
    assert product.quantity == 10


def test_new_product():
    product_data = {
        "name": "Новый товар",
        "description": "Описание нового товара",
        "price": 100.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)
    assert product.name == "Новый товар"
    assert product.description == "Описание нового товара"
    assert product.price == 100.0
    assert product.quantity == 5


def test_price_getter_and_setter():
    product = Product("Тестовый товар", "Описание", 100.0, 5)
    assert product.price == 100.0  # Проверка геттера

    product.price = -50.0  # Некорректная цена
    assert product.price == 100.0  # Цена не должна измениться

    product.price = 150.0  # Корректная цена
    assert product.price == 150.0  # Проверка установки новой цены
