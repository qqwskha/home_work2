# E-commerce
Проект представляет собой ядро для интернет магазина на языке программирования Python

## Функциональность

- **Класс `Product`**: Описывает товары с атрибутами:
  - `name` — название товара,
  - `description` — описание товара,
  - `price` — цена товара,
  - `quantity` — количество товара в наличии.
- **Методы**:
  - `__str__`: Возвращает строковое представление товара в формате:
  `"Название продукта, X руб. Остаток: X шт."`
  - `__add__`: Позволяет складывать товары одного типа, возвращая полную стоимость всех товаров на складе.

- **Класс `Category`**: Описывает категории товаров с атрибутами:
  - `name` — название категории,
  - `description` — описание категории,
  - `products` — список товаров в категории.
- **Методы**:
- `add_product`: Добавляет товар в категорию с проверкой типа объекта.
- `__str__`: Возвращает строковое представление категории в формате:
`"Название категории, количество продуктов: X шт."`

- **Классы наследники**:
- `Smartphone`:
  * Расширяет класс `Product` следующими атрибутами:
    * `efficiency` — производительность,
    * `model` — модель,
    * `memory` — объем встроенной памяти,
    * `color` — цвет.
- `LawnGrass`:
  * Расширяет класс `Product` следующими атрибутами:
    * `country` — страна-производитель,
    * `germination_period` — срок прорастания,
    * `color` — цвет.

- **Ограничения добавления продукта**:
* Метод `add_product` в классе `Category` проверяет, что добавляемый объект является экземпляром класса Product или его наследников. 
* При попытке добавить объект другого типа выбрасывается ошибка TypeError.


- **Автоматический подсчет**:
  - Количество категорий (`category_count`).
  - Количество товаров (`product_count`).

- **Загрузка данных из JSON**: Реализована функция `load_categories_from_json`, которая загружает данные о категориях и товарах из JSON-файла.

## Установка и запуск

1. Убедитесь, что у вас установлен Python 3.11 или выше.
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/qqwskha/home_work2.git
   
# Пример использования
```python
from src.category import Category, load_categories_from_json
from src.product import Product
```

## Создание товаров
```python
product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)
product2 = Product("Смартфон", "Смартфон с OLED-экраном", 699.99, 15)
```

## Создание категории
```python
electronics = Category("Электроника", "Техника для дома и офиса", [product1, product2])
```

## Загрузка данных из JSON
```python
categories = load_categories_from_json("products.json")
```

## Создание товаров
```python
from src.product import Product, Smartphone, LawnGrass

# Базовый продукт
product = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 10)

# Смартфон
smartphone = Smartphone(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
    95.5, "S23 Ultra", 256, "Серый"
)

# Газонная трава
grass = LawnGrass(
    "Газонная трава", "Элитная трава для газона", 500.0, 20,
    "Россия", "7 дней", "Зеленый"
)
```

## Создание категории

```python
from src.category import Category

electronics = Category("Электроника", "Техника для дома и офиса", [smartphone])
electronics.add_product(product)
```

## Сложение товаров
```python
# Сложение товаров одного типа
total_cost = smartphone + smartphone
print(total_cost)  # Полная стоимость всех товаров на складе

# Попытка сложить товары разных типов
try:
    invalid_sum = smartphone + grass
except TypeError as e:
    print(e)  # "Нельзя складывать объекты разных типов"
```
