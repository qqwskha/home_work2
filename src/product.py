class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
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

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if hasattr(self, '_Product__price') and new_price < self.__price:
                confirmation = input("Цена снижается. Подтвердите действие (y/n): ")
                if confirmation.lower() != 'y':
                    print("Изменение цены отменено.")
                    return
            self.__price = new_price

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод сложения двух продуктов."""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Нельзя складывать объекты разных типов")