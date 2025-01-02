import pytest
from challenge import Solution  # Importa la clase Solution desde tu archivo de reto

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "operations, expected_output",
        [
            (["5", "2", "C", "D", "+"], 30),                      # Ejemplo de operaciones típicas
            (["5", "2", "D", "+"], 30),                            # Evaluación con el caso 'D' y '+'
            (["5", "-2", "C", "D", "+"], 15),                      # Con valores negativos
            (["1", "C"], 0),                                      # Se cancela la operación por "C"
            (["D", "C", "+", "D", "10"], 30),                      # Varios movimientos válidos y cancelados
            (["1", "1", "+"], 3),                                  # Evaluación con el operador "+"
            (["10", "10", "C"], 10),                              # Casos con "C" eliminando operaciones
            (["D"], 0),                                           # Caso donde no hay operaciones antes de 'D'
            (["5", "C", "C", "5"], 5),                            # Repetir eliminaciones con 'C'
            ([], 0),                                              # Caso con operaciones vacías
        ]
    )
    def test_calPoints(self, operations, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función calPoints.

        Args:
            operations (List[str]): La lista de operaciones realizadas durante la partida.
            expected_output (int): El total esperado de puntos después de procesar todas las operaciones.
        """
        assert self.solution.calPoints(operations) == expected_output
