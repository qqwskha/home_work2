from src.product import LawnGrass, Product, Smartphone


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


def test_product_str():
    product = Product("Тестовый товар", "Описание", 100.0, 5)
    assert str(product) == "Тестовый товар, 100.0 руб. Остаток: 5 шт."


def test_product_addition():
    product1 = Product("Товар 1", "Описание", 100.0, 10)
    product2 = Product("Товар 2", "Описание", 200.0, 5)
    assert product1 + product2 == 2000.0


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


def test_addition_same_class():
    smartphone1 = Smartphone("Samsung", "Desc", 100.0, 10, 90.0, "Model", 128, "Black")
    smartphone2 = Smartphone("Apple", "Desc", 200.0, 5, 95.0, "Model", 256, "White")
    assert smartphone1 + smartphone2 == 2000.0


def test_addition_different_classes():
    smartphone = Smartphone("Samsung", "Desc", 100.0, 10, 90.0, "Model", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 50.0, 20, "USA", "5 days", "Green")
    try:
        smartphone + grass
    except TypeError as e:
        assert str(e) == "Нельзя складывать объекты разных типов"
