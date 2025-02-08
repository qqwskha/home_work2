import json
from src.category import Category, load_categories_from_json
from src.product import Product
import pytest

@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасывает глобальные счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0

def test_category_initialization():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])

    assert electronics.name == "Электроника"
    assert electronics.description == "Техника для дома и офиса"
    assert len(electronics.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_valid_product():
    category = Category("Test", "Description", [])
    product = Product("Test Product", "Desc", 100.0, 5)
    category.add_product(product)
    assert len(category.products) == 1
    assert Category.product_count == 1


def test_add_invalid_product():
    category = Category("Test", "Description", [])
    invalid_product = "Not a product"
    try:
        category.add_product(invalid_product)
    except TypeError as e:
        assert str(e) == "В категорию можно добавлять только объекты класса Product или его наследников"


def test_products_property():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])
    assert electronics.products == [product1, product2]


def test_get_products_info():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])
    expected_output = (
        "Ноутбук, 999.99 руб. Остаток: 10 шт.\n"
        "Смартфон, 699.99 руб. Остаток: 15 шт."
    )
    assert electronics.get_products_info() == expected_output


def test_category_str():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])
    assert str(electronics) == "Электроника, количество продуктов: 25 шт."


def test_load_categories_from_json(tmpdir):
    # Создаем временный JSON-файл
    test_data = [
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
    file_path = tmpdir.join("test_products.json")
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_data, file)

    # Загружаем данные
    categories = load_categories_from_json(file_path)
    assert len(categories) == 1
    category = categories[0]
    assert category.name == "Тестовая категория"
    assert category.description == "Описание тестовой категории"
    assert len(category.products) == 1
    assert category.products[0].name == "Тестовый товар"


def test_load_categories_from_invalid_json(tmpdir):
    # Создаем некорректный JSON-файл
    invalid_data = "invalid json"
    file_path = tmpdir.join("invalid.json")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(invalid_data)

    try:
        load_categories_from_json(file_path)
    except json.JSONDecodeError:
        assert True
    else:
        assert False, "Ожидалась ошибка JSONDecodeError"


def test_empty_category():
    empty_category = Category("Пустая категория", "Описание", [])
    assert len(empty_category.products) == 0
    assert str(empty_category) == "Пустая категория, количество продуктов: 0 шт."
    assert empty_category.get_products_info() == ""

def test_load_categories_with_missing_fields(tmpdir):
    # Создаем JSON-файл с отсутствующими полями
    invalid_data = [
        {
            "name": "Тестовая категория",
            "description": "Описание тестовой категории",
            "products": [
                {
                    "name": "Тестовый товар",  # Отсутствует "description"
                    "price": 100.0,
                    "quantity": 10
                }
            ]
        }
    ]
    file_path = tmpdir.join("invalid_products.json")
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(invalid_data, file)

    try:
        load_categories_from_json(file_path)
    except KeyError as e:
        assert str(e) == "'description'"


def test_private_products_attribute():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    electronics = Category("Электроника", "Техника для дома и офиса", [product1])
    assert hasattr(electronics, '_Category__products')  # Проверка наличия приватного атрибута
    assert electronics._Category__products == [product1]  # Прямой доступ к приватному атрибуту
