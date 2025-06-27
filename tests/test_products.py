import pytest
from product import Product, Category, ZeroQuantityError


class TestProduct:
    def test_init_with_zero_quantity(self):

        with pytest.raises(ZeroQuantityError):
            Product("Test", 100, 0)

    def test_init_with_positive_quantity(self, capsys):

        p = Product("Test", 100, 10)
        out, _ = capsys.readouterr()
        assert "Товар 'Test' успешно добавлен" in out
        assert "Обработка добавления товара завершена" in out


class TestCategory:
    def test_average_price_with_products(self):

        category = Category("Test")
        category.add_product(Product("A", 100, 5))
        category.add_product(Product("B", 200, 3))
        assert category.average_price() == 150.0

    def test_average_price_empty(self):

        category = Category("Test")
        assert category.average_price() == 0.0

    def test_add_zero_quantity_product(self, capsys):

        category = Category("Test")
        with pytest.raises(ZeroQuantityError):
            category.add_product(Product("Zero", 50, 0))
        out, _ = capsys.readouterr()
        assert "не может быть добавлен" in out
