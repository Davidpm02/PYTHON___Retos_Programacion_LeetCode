import pytest
from challenge import Solution  # Asegúrate de que el archivo se llame challenge.py y la clase Solution esté definida allí.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "moves, expected_output",
        [
            # Casos en los que el robot vuelve a la posición original (True)
            ("UD", True),                   # Un movimiento hacia arriba y otro hacia abajo
            ("LR", True),                   # Un movimiento hacia la izquierda y otro hacia la derecha
            ("UDLR", True),                 # Combinación de movimientos
            ("UUDDLLRR", True),             # Los movimientos forman un círculo, volviendo al origen
            ("", True),                     # El robot no se mueve, por lo que siempre vuelve al origen
            ("RRUUUULLLL", True),           # Movimiento hacia la derecha y luego hacia arriba, izquierda

            # Casos en los que el robot no vuelve a la posición original (False)
            ("U", False),                   # El robot sube pero no realiza más movimientos, por lo que no vuelve al origen
            ("LL", False),                  # El robot se mueve solo a la izquierda, no vuelve al origen
            ("URDL", False),                # El robot hace un desplazamiento que no regresa al origen
            ("UUURRR", False),              # El robot se mueve de forma que no regresa a la posición inicial
        ]
    )
    def test_judgeCircle(self, moves, expected_output):
        """
        Prueba parametrizada para validar si un robot regresa o no a su posición inicial.

        Args:
            moves (str): La secuencia de movimientos del robot.
            expected_output (bool): El resultado esperado (True si regresa al origen, False si no).
        """
        assert self.solution.judgeCircle(moves) == expected_output
