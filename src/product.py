class ZeroQuantityError(Exception):
    
    pass


class Product:
    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        try:
            if quantity == 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
            self.quantity = quantity
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
            raise
        else:
            print(f"Товар '{name}' успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        """Добавление товара в категорию"""
        self.products.append(product)

    def average_price(self) -> float:

        try:
            total = sum(product.price for product in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0.0