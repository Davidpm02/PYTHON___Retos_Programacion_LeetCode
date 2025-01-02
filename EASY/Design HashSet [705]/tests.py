import pytest
from challenge import MyHashSet  # Importa la clase MyHashSet desde el módulo correspondiente


class TestMyHashSet:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de MyHashSet antes de cada prueba."""
        self.hash_set = MyHashSet()

    def test_add_and_contains(self):
        """Prueba de agregar elementos con `add` y verificar su existencia con `contains`."""
        # Agregamos claves al conjunto
        self.hash_set.add(1)
        self.hash_set.add(2)
        
        # Verificamos que los elementos fueron añadidos
        assert self.hash_set.contains(1) == True  # El conjunto contiene '1'
        assert self.hash_set.contains(2) == True  # El conjunto contiene '2'

    def test_remove(self):
        """Prueba de remover elementos con `remove` y luego verificar su ausencia con `contains`."""
        # Agregamos un elemento
        self.hash_set.add(1)
        
        # Verificamos que el elemento existe
        assert self.hash_set.contains(1) == True
        
        # Removemos el elemento
        self.hash_set.remove(1)
        
        # Verificamos que el elemento ya no existe en el conjunto
        assert self.hash_set.contains(1) == False

    def test_remove_non_existent_key(self):
        """Prueba de intentar eliminar una clave que no existe en el conjunto."""
        # Intentamos remover una clave que no ha sido añadida
        self.hash_set.remove(5)  # No existe la clave 5
        
        # Verificamos que el conjunto sigue en su estado original (sin claves)
        assert self.hash_set.contains(5) == False  # No debería contener 5

    def test_contains_empty_set(self):
        """Prueba de verificar `contains` cuando el conjunto está vacío."""
        # Verificamos que no hay elementos en el conjunto inicialmente
        assert self.hash_set.contains(1) == False  # El conjunto no contiene la clave 1 al principio
