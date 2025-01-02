import pytest
from challenge import MyHashMap


class TestMyHashMap:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de MyHashMap antes de cada prueba."""
        self.hash_map = MyHashMap()

    def test_put_and_get(self):
        """Prueba de la inserción de claves con `put` y su obtención con `get`."""
        # Insertamos un par de clave-valor
        self.hash_map.put(1, 10)
        self.hash_map.put(2, 20)
        
        # Verificamos que los valores sean los correctos
        assert self.hash_map.get(1) == 10
        assert self.hash_map.get(2) == 20

    def test_get_key_not_found(self):
        """Prueba de la función `get` para una clave que no está en el mapa."""
        # Comprobamos que obtendremos -1 si no existe la clave
        assert self.hash_map.get(3) == -1  # 3 no está en el hash_map

    def test_remove(self):
        """Prueba de la función `remove` para eliminar una clave del mapa."""
        # Insertamos un par clave-valor
        self.hash_map.put(1, 10)
        
        # Comprobamos que la clave existe y tiene el valor correcto
        assert self.hash_map.get(1) == 10
        
        # Eliminamos la clave
        self.hash_map.remove(1)
        
        # Comprobamos que la clave ha sido eliminada
        assert self.hash_map.get(1) == -1  # Debería retornar -1 porque la clave fue eliminada

    def test_remove_non_existent_key(self):
        """Prueba de eliminar una clave que no existe en el mapa."""
        # Intentamos eliminar una clave inexistente
        self.hash_map.remove(5)  # No existe una clave '5'
        
        # Verificamos que no hay cambios en el mapa (sigue vacío)
        assert self.hash_map.get(5) == -1  # La clave 5 debería seguir siendo -1
        assert self.hash_map.get(1) == -1  # Verificamos otras claves también
