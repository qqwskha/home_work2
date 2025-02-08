from unittest.mock import patch

import pytest

from src.product import BaseProduct, Product, Smartphone, LawnGrass


def test_base_product_initialization():
    class TestProduct(BaseProduct):
        def __init__(self, name: str, description: str, price: float, quantity: int):
            self.name = name
            self.description = description
            self.price = price
            self.quantity = quantity

        def __str__(self):
            return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

        def get_total_price(self) -> float:
            return self.price * self.quantity

    product = TestProduct("Тестовый продукт", "Описание", 100.0, 5)
    assert product.name == "Тестовый продукт"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 5
    assert product.get_total_price() == 500.0


# Тестирование класса Product
def test_product_initialization():
    product = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой ноутбук"
    assert product.price == 999.99
    assert product.quantity == 10


def test_product_price_getter_and_setter():
    product = Product("Тестовый товар", "Описание", 100.0, 5)
    assert product.price == 100.0  # Проверка геттера

    product.price = -50.0  # Некорректная цена
    assert product.price == 100.0  # Цена не должна измениться

    product.price = 150.0  # Корректная цена
    assert product.price == 150.0  # Проверка установки новой цены


def test_product_str():
    product = Product("Тестовый товар", "Описание", 100.0, 5)
    assert str(product) == "Тестовый товар, 100.0 руб. Остаток: 5 шт."


def test_product_addition():
    product1 = Product("Товар 1", "Описание", 100.0, 10)
    product2 = Product("Товар 2", "Описание", 200.0, 5)
    assert product1 + product2 == 2000.0


def test_product_addition_invalid_type():
    product = Product("Товар", "Описание", 100.0, 5)
    invalid_object = "Не продукт"
    try:
        product + invalid_object
    except TypeError as e:
        assert str(e) == "Нельзя складывать объекты разных типов"


# Тестирование класса Smartphone
def test_smartphone_creation():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
        95.5, "S23 Ultra", 256, "Серый"
    )
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


# Тестирование класса LawnGrass
def test_lawn_grass_creation():
    grass = LawnGrass(
        "Газонная трава", "Элитная трава для газона", 500.0, 20,
        "Россия", "7 дней", "Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


# Тестирование наследования от Product
def test_inheritance():
    smartphone = Smartphone("iPhone", "Smartphone", 1000.0, 1, 90.0, "Model", 128, "Black")
    grass = LawnGrass("Grass", "Lawn Grass", 50.0, 10, "USA", "5 days", "Green")

    assert isinstance(smartphone, Product)
    assert isinstance(grass, Product)

    assert smartphone.get_total_price() == 1000.0
    assert grass.get_total_price() == 500.0

def test_price_setter_with_confirmation():
    product = Product("Тестовый товар", "Описание", 100.0, 5)
    with patch('builtins.input', return_value='y'):
        product.price = 80.0
        assert product.price == 80.0

    with patch('builtins.input', return_value='n'):
        product.price = 70.0
        assert product.price == 80.0  # Цена не должна измениться


def test_addition_different_types():
    product = Product("Товар", "Описание", 100.0, 5)
    invalid_object = "Не продукт"
    try:
        product + invalid_object
    except TypeError as e:
        assert str(e) == "Нельзя складывать объекты разных типов"


def test_private_price_attribute():
    product = Product("Тестовый товар", "Описание", 100.0, 5)
    assert hasattr(product, '_Product__price')  # Проверка наличия приватного атрибута
    assert product._Product__price == 100.0  # Прямой доступ к приватному атрибуту


def test_smartphone_all_attributes():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
        95.5, "S23 Ultra", 256, "Серый"
    )
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_all_attributes():
    grass = LawnGrass(
        "Газонная трава", "Элитная трава для газона", 500.0, 20,
        "Россия", "7 дней", "Зеленый"
    )
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_product_creation_with_zero_quantity():
    """Проверка создания товара с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_creation_with_positive_quantity():
    """Проверка создания товара с положительным количеством."""
    product = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
    assert product.quantity == 10

