import pytest
from challenge import Solution  # Importamos la clase Solution desde el archivo challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "colors, k, expected_output",
        [
            ([0,1,0,1,0], 3, 3),  # Caso con grupos alternantes claramente definidos
            ([0,1,0,0,1,0,1], 6, 2),  # Caso con una mayor cantidad de elementos
            ([1,1,0,1], 4, 0),  # Caso sin grupos alternantes válidos
            ([0,1,0,1,0,1,0,1], 4, 5),  # Caso con patrón perfectamente alternante
            ([0,0,0,0,0], 3, 0),  # Caso con todos los elementos iguales (sin alternancia)
            ([1,0,1,0,1,0,1,0,1,0], 5, 6),  # Caso con una secuencia de alternancia regular
            ([1,1,1,0,1,1,1], 3, 0),  # Caso con una interrupción en la alternancia
            ([0,1,0,1,0,1,0,1,0,1,0,1], 6, 7),  # Caso con secuencia alternante larga
            ([1,0,1,0,1,0,1,0,1], 9, 1),  # Caso donde toda la lista es un solo grupo alternante
        ]
    )
    def test_number_of_alternating_groups(self, colors, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función numberOfAlternatingGroups.

        Args:
            colors (List[int]): La lista de colores representando el círculo.
            k (int): Tamaño del grupo alternante.
            expected_output (int): El número esperado de grupos alternantes.
        """
        assert self.solution.numberOfAlternatingGroups(colors, k) == expected_output