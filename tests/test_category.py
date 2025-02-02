import json

from src.category import Category, load_categories_from_json
from src.product import Product


def test_category_initialization():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])
    assert electronics.name == "Электроника"
    assert electronics.description == "Техника для дома и офиса"
    assert len(electronics._Category__products) == 2  # Проверяем длину приватного списка


def test_category_count():
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])
    assert electronics.name == "Электроника"

    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2


def test_load_categories_from_json():
    # Создаем временный JSON-файл
    test_json = [
        {
            "name": "Тестовая категория",
            "description": "Описание тестовой категории",
            "products": [
                {
                    "name": "Тестовый товар",
                    "description": "Описание тестового товара",
                    "price": 100.0,
                    "quantity": 10
                }
            ]
        }
    ]
    with open("test_products.json", "w", encoding="utf-8") as file:
        json.dump(test_json, file)
    # Загружаем данные
    categories = load_categories_from_json("test_products.json")
    # Проверяем результат
    assert len(categories) == 1
    assert categories[0].name == "Тестовая категория"
    assert len(categories[0]._Category__products) == 1  # Проверяем длину приватного списка


def test_category_str():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])
    assert str(electronics) == "Электроника, количество продуктов: 25 шт."


def test_add_valid_product():
    category = Category("Test", "Description", [])
    product = Product("Test Product", "Desc", 100.0, 5)
    category.add_product(product)
    assert len(category._Category__products) == 1


def test_add_invalid_product():
    category = Category("Test", "Description", [])
    invalid_product = "Not a product"
    try:
        category.add_product(invalid_product)
    except TypeError as e:
        assert str(e) == "В категорию можно добавлять только объекты класса Product или его наследников"
