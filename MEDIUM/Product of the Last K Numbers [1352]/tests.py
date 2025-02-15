import pytest
from challenge import ProductOfNumbers  

class TestProductOfNumbers:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase ProductOfNumbers antes de cada prueba."""
        self.product_of_numbers = ProductOfNumbers()

    def test_add_and_get_product(self):
        """Prueba la funcionalidad de add y getProduct."""
        self.product_of_numbers.add(3)
        self.product_of_numbers.add(2)
        self.product_of_numbers.add(5)
        assert self.product_of_numbers.getProduct(1) == 5  # Último elemento
        assert self.product_of_numbers.getProduct(2) == 10 # 5 * 2
        assert self.product_of_numbers.getProduct(3) == 30 # 5 * 2 * 3

    def test_get_product_with_zero(self):
        """Verifica el comportamiento cuando se agrega un 0."""
        self.product_of_numbers.add(3)
        self.product_of_numbers.add(0)
        self.product_of_numbers.add(2)
        self.product_of_numbers.add(5)
        assert self.product_of_numbers.getProduct(1) == 5  # Último elemento
        assert self.product_of_numbers.getProduct(2) == 10 # 5 * 2
        assert self.product_of_numbers.getProduct(3) == 0  # Se encuentra un 0

    def test_get_product_edge_cases(self):
        """Prueba casos límite como pedir el producto de más elementos de los existentes."""
        self.product_of_numbers.add(7)
        assert self.product_of_numbers.getProduct(1) == 7  # Único elemento
        assert self.product_of_numbers.getProduct(2) == 0  # Se excede el rango, debe devolver 0

    def test_consecutive_zeros(self):
        """Prueba el comportamiento con múltiples ceros consecutivos."""
        self.product_of_numbers.add(0)
        self.product_of_numbers.add(0)
        self.product_of_numbers.add(3)
        assert self.product_of_numbers.getProduct(1) == 3  # Último número
        assert self.product_of_numbers.getProduct(2) == 0  # Se encuentra un 0
        assert self.product_of_numbers.getProduct(3) == 0  # Se encuentra un 0
