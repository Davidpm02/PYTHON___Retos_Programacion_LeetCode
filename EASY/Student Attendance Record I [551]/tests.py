import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("PPALLP", True),     # Caso válido: un alumno con buena asistencia
            ("PPALLL", False),    # Caso inválido: alumno con 3 tardanzas consecutivas
            ("PPALLA", False),    # Caso inválido: alumno con más de una ausencia
            ("P", True),          # Caso válido: solo una asistencia
            ("A", True),          # Caso válido: una única ausencia
            ("AA", False),        # Caso inválido: dos ausencias
            ("LLL", False),       # Caso inválido: solo tardanzas consecutivas
            ("", True),           # Caso válido: historial vacío
            ("PLPLP", True),      # Caso válido: sin tardanzas consecutivas ni múltiples ausencias
            ("PALLPLL", True),    # Caso válido: dos tardanzas consecutivas pero no tres
        ]
    )
    def test_check_record(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función checkRecord.

        Args:
            input_str (str): Historial de asistencia del alumno.
            expected_output (bool): Resultado esperado sobre si merece o no un premio.
        """
        assert self.solution.checkRecord(input_str) == expected_output
