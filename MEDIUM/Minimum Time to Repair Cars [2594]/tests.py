import pytest
from challenge import Solution  # Importamos la clase Solution desde el archivo principal


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "ranks, cars, expected_output",
        [
            ([4, 2, 3], 4, 6),   # Caso básico con mecánicos de distintos rangos
            ([5, 1, 8], 10, 25), # Caso con más coches y distintos rangos
            ([10], 5, 250),      # Un solo mecánico con un rango alto
            ([1, 2, 3, 4], 10, 16), # Varios mecánicos con diferentes rangos
            ([2, 3, 5], 7, 15),  # Combinación de mecánicos con números primos
            ([1], 1, 1),         # Caso mínimo con un solo mecánico y un coche
            ([100, 200, 300], 1, 100), # Caso donde el mecánico con menor rango debería reparar el coche
            ([3, 7, 11], 15, 77), # Caso con diferentes rangos y un número mayor de coches
        ]
    )
    def test_repair_cars(self, ranks, cars, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función repairCars.

        Args:
            ranks (List[int]): Lista de rangos de los mecánicos.
            cars (int): Número total de coches a reparar.
            expected_output (int): Resultado esperado en tiempo mínimo.
        """
        assert self.solution.repairCars(ranks, cars) == expected_output
