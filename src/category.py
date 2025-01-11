class Category:
    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0   # Атрибут класса для подсчета товаров

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)
