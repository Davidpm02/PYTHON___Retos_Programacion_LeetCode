import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "differences, lower, upper, expected_output",
        [
            ([1, -3, 4], 1, 6, 2),                   # Dos posibles secuencias dentro del rango
            ([3, -4, 5, 1, -2], -4, 5, 2),            # Dos valores iniciales que generan secuencias válidas
            ([4, -7, 2], 3, 6, 0),                   # No hay ningún valor inicial válido
            ([], 0, 0, 1),                           # Caso borde: array vacío (único valor 0)
            ([1, 1, 1], -100, 100, 199),              # Rango muy amplio, muchas opciones válidas
            ([-1, -1, -1], -3, 0, 1),                 # Acumulando negativos dentro de un rango ajustado
            ([2, -2, 2, -2], 0, 0, 1),                # El acumulado siempre vuelve a 0
            ([0, 0, 0], -1, 1, 3),                    # Las diferencias son todas 0, tres posibles valores iniciales
            ([5], -10, 10, 6),                        # Solo un valor en differences, varias opciones
            ([1, 2, 3], 0, 6, 1),                     # Solo una opción de secuencia completa dentro del rango
        ]
    )
    def test_number_of_arrays(self, differences, lower, upper, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función numberOfArrays.

        Args:
            differences (List[int]): Lista de diferencias a aplicar.
            lower (int): Límite inferior permitido para los valores de la secuencia.
            upper (int): Límite superior permitido para los valores de la secuencia.
            expected_output (int): Número esperado de secuencias posibles.
        """
        assert self.solution.numberOfArrays(differences, lower, upper) == expected_output
