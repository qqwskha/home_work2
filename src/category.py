import json
from abc import ABC, abstractmethod
from src.product import Product

class BaseEntity(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Category(BaseEntity):
    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0   # Атрибут класса для подсчета товаров

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)

    def middle_price(self):
        """Вычисляет среднюю цену всех товаров в категории."""
        if not self.products:
            return 0  # Если товаров нет, возвращаем 0
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)

    def add_product(self, product):
        """Добавляет товар в приватный список продуктов."""
        if isinstance(product, Product):  # Проверяем, что объект является продуктом
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников")

    @property
    def products(self):
        """Геттер для получения списка товаров."""
        return self.__products

    def get_products_info(self):
        """Возвращает строку с информацией о товарах."""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


def load_categories_from_json(file_path: str):
    """
    Загружает данные о категориях и товарах из JSON-файла.
    Возвращает список объектов Category.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    categories = []
    for category_data in data:
        # Создаем список товаров для категории
        products = [
            Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"]
            )
            for product_data in category_data["products"]
        ]
        # Создаем объект Category
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)
    return categories