import pytest
from challenge import Solution  # Ajusta el import según el nombre de tu archivo.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "bills, expected_output",
        [
            ([5, 5, 5, 10, 20], True),              # Caso típico donde podemos dar el cambio
            ([5, 5, 10], True),                    # El cliente con billete de 10 puede recibir cambio
            ([10, 5], False),                      # No se puede devolver cambio al cliente con 10
            ([5, 5, 10, 10, 20], False),           # No hay suficiente cambio para el segundo cliente con 10
            ([5, 5, 5, 10, 10, 20], True),         # Al llegar al cliente con 20 se tiene suficiente cambio
            ([5, 5, 20], False),                   # No se puede dar el cambio al cliente con 20
            ([10, 20], False),                     # El primer cliente tiene billete de 10 y no se tiene cambio
            ([5, 5, 5, 10], True),                 # El cliente con billete de 10 puede recibir cambio
            ([5, 10, 5, 10, 20], True),            # Caso con diferentes combinaciones
            ([5, 10, 5, 20, 5, 10], True),         # Caso con múltiples 5, 10 y 20, pero sin problema para dar el cambio
            ([5, 10, 5, 10, 10, 5], False),        # No hay suficiente cambio para la segunda persona con 10
        ]
    )
    def test_lemonadeChange(self, bills, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función lemonadeChange.

        Args:
            bills (List[int]): La lista de billetes que los clientes pagan.
            expected_output (bool): True si se puede devolver el cambio correctamente, False si no.
        """
        assert self.solution.lemonadeChange(bills) == expected_output
