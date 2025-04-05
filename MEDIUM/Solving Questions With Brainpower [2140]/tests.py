import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "questions, expected_output",
        [
            ([[3, 2], [4, 3], [5, 2], [8, 1], [1, 1]], 12),   # Casos donde elegir sabiamente entre resolver o saltar da el máximo puntaje
            ([[3, 1], [2, 2], [4, 0]], 7),                      # Resolver todas las preguntas da más puntos que saltar
            ([[1, 1], [2, 1], [3, 1], [4, 1]], 7),              # Caso sencillo donde siempre es mejor resolver las preguntas
            ([[10, 2], [5, 1], [2, 0]], 12),                    # Preguntas con diferentes combinaciones de puntajes y saltos
            ([[10, 0]], 10),                                    # Solo hay una pregunta, el puntaje es el mismo
            ([[5, 1], [1, 0], [10, 0]], 15),                    # Resolvemos la primera y tercera pregunta para obtener el puntaje máximo
            ([[1, 1], [1, 1], [1, 1], [1, 1]], 4),              # Caso con múltiples preguntas con puntajes pequeños
            ([[5, 2], [5, 1], [5, 0], [5, 0]], 15),             # Solo podemos resolver algunas preguntas debido a las restricciones de saltar
            ([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]], 12),    # Escenario donde se pueden resolver varias preguntas en secuencia
            ([[1, 1], [2, 2], [3, 3], [4, 4]], 6),              # Escenario con preguntas que requieren saltar muchas veces
            ([[1, 2], [1, 2], [1, 2], [1, 2]], 4),              # Preguntas de valor pequeño con saltos largos
        ]
    )
    def test_most_points(self, questions, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método mostPoints.

        Args:
            questions (List[List[int]]): Lista de preguntas con sus puntos y número de preguntas a saltar.
            expected_output (int): La puntuación máxima esperada.
        """
        assert self.solution.mostPoints(questions) == expected_output
