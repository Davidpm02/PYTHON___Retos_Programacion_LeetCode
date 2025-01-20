import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, locked, expected_output",
        [
            ("()", "11", True),                      # Caso simple de paréntesis válidos bloqueados
            (")(", "11", False),                    # Paréntesis en orden incorrecto y bloqueados
            ("(())", "1111", True),                 # Estructura válida completamente bloqueada
            ("(())", "0000", True),                 # Todos desbloqueados, se pueden organizar
            ("(()", "101", True),                   # Algunos desbloqueados que permiten hacerlos válidos
            ("(()", "111", False),                  # Falta un paréntesis pero todos están bloqueados
            ("())", "101", True),                   # Estructura válida ajustando los desbloqueados
            ("(()))", "11001", False),              # Más paréntesis de cierre de los necesarios
            ("(()))", "11000", True),               # Se ajusta gracias a los desbloqueados
            ("", "", True),                         # Cadena vacía siempre válida
            ("((", "10", False),                    # Número de paréntesis impar, inválido
            ("))((", "0000", False),                # Imposible hacerlos válidos
            ("()", "00", True),                     # Totalmente desbloqueado
            ("(()())", "101010", True),             # Alternancia de bloqueos que permite ajuste
            ("(()(()))", "11111111", True),         # Complejo pero válido y bloqueado
            ("(()(()))", "11001001", True),         # Caso complejo con desbloqueo parcial
        ]
    )
    def test_can_be_valid(self, s, locked, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función canBeValid.

        Args:
            s (str): Cadena de entrada con paréntesis.
            locked (str): Indica qué caracteres están bloqueados ('1') o desbloqueados ('0').
            expected_output (bool): Resultado esperado de la función.
        """
        assert self.solution.canBeValid(s, locked) == expected_output
