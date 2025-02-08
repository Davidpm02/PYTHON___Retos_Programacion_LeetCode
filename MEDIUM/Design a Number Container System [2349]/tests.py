import pytest
from challenge import NumberContainers  # Asegúrate de que el archivo donde tienes el código se llama challenge.py

class TestNumberContainers:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase NumberContainers antes de cada prueba."""
        self.solution = NumberContainers()

    def test_change_and_find(self):
        """Prueba para validar las operaciones change y find."""
        
        # Insertamos algunos valores
        self.solution.change(1, 10)
        self.solution.change(2, 20)
        self.solution.change(3, 10)
        
        # Verificamos que find devuelve el índice correcto
        assert self.solution.find(10) == 1  # El índice de 10 debe ser 1 (el más pequeño)
        assert self.solution.find(20) == 2  # El índice de 20 debe ser 2
        assert self.solution.find(30) == -1  # El número 30 no ha sido insertado, debe devolver -1

    def test_lazy_deletion(self):
        """Prueba para validar la eliminación perezosa cuando se encuentra un índice obsoleto."""
        
        # Insertamos algunos valores
        self.solution.change(1, 10)
        self.solution.change(2, 10)
        self.solution.change(3, 10)
        self.solution.change(4, 20)
        
        # Eliminamos el índice 1 y cambiamos el valor
        self.solution.change(1, 30)
        
        # Ahora el índice 1 debería retornar -1 al buscar el número 10
        assert self.solution.find(10) == 2  # El índice más pequeño para 10 debería ser 2
        
        # El número 30 debería estar asociado al índice 1
        assert self.solution.find(30) == 1
        
        # El número 20 debe devolver el índice 4
        assert self.solution.find(20) == 4

    def test_edge_cases(self):
        """Pruebas de bordes y casos extremos."""
        
        # Casos con números no insertados
        assert self.solution.find(999) == -1  # El número 999 no existe en el contenedor
        assert self.solution.find(0) == -1    # El número 0 no existe en el contenedor
        
        # Casos con inserciones repetidas en el mismo índice
        self.solution.change(1, 100)
        self.solution.change(1, 200)  # Cambiamos el valor en el mismo índice
        
        # Verificamos que la búsqueda de 100 devuelva -1, ya que se cambió por 200
        assert self.solution.find(100) == -1
        
        # Verificamos que la búsqueda de 200 devuelva el índice 1
        assert self.solution.find(200) == 1

    def test_multiple_changes_and_finds(self):
        """Prueba para validar múltiples cambios y búsquedas."""
        
        # Insertamos valores y cambiamos repetidamente
        self.solution.change(1, 50)
        self.solution.change(2, 60)
        self.solution.change(3, 50)
        self.solution.change(4, 50)
        self.solution.change(5, 60)
        
        # Verificamos que el número 50 retorne el índice más bajo (1)
        assert self.solution.find(50) == 1
        
        # Verificamos que el número 60 retorne el índice más bajo (2)
        assert self.solution.find(60) == 2
        
        # Modificamos algunos valores
        self.solution.change(1, 70)
        self.solution.change(2, 80)
        
        # Verificamos que después de los cambios, los índices correctos sean retornados
        assert self.solution.find(50) == 3  # El índice 50 ahora es 3
        assert self.solution.find(60) == 5  # El índice 60 ahora es 5

