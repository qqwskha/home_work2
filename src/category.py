import json
from product import Product


class Category:
    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0   # Атрибут класса для подсчета товаров

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет товар в приватный список продуктов."""
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик товаров


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
