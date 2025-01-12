# E-commerce
Проект представляет собой ядро для интернет магазина на языке программирования Python

## Функциональность

- **Класс `Product`**: Описывает товары с атрибутами:
  - `name` — название товара,
  - `description` — описание товара,
  - `price` — цена товара,
  - `quantity` — количество товара в наличии.

- **Класс `Category`**: Описывает категории товаров с атрибутами:
  - `name` — название категории,
  - `description` — описание категории,
  - `products` — список товаров в категории.

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