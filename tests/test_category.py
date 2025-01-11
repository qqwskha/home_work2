from src.category import Category
from src.product import Product


def test_category_initialization():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])

    assert electronics.name == "Электроника"
    assert electronics.description == "Техника для дома и офиса"
    assert len(electronics.products) == 2


def test_category_count():
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])

    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2