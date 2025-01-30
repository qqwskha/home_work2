class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


@classmethod
def new_product(cls, product_data: dict):
    """
    Создает новый продукт на основе данных из словаря.
    :param product_data: Словарь с данными продукта.
    :return: Экземпляр класса Product.
    """
    return cls(
        name=product_data["name"],
        description=product_data.get("description", ""),
        price=product_data["price"],
        quantity=product_data["quantity"]
    )