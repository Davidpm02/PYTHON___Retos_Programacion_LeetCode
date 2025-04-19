import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, 5),                          # Solo una posición par, 5 posibles dígitos válidos
            (2, 20),                         # 1 par (5 opciones) * 1 impar (4 opciones) = 20
            (3, 100),                        # 2 pares (5^2=25) * 1 impar (4) = 100
            (4, 400),                        # 2 pares (25) * 2 impares (16) = 400
            (50, 564908303),                # Valor grande comprobado contra solución esperada
            (0, 1),                          # Caso borde: 0 dígitos => 1 número válido (vacío)
            (10**5, None),                  # Solo comprobamos que no rompe y da resultado bajo el límite de tiempo
        ]
    )
    def test_count_good_numbers(self, n, expected_output):
        """
        Prueba parametrizada para verificar la cantidad de números 'buenos' que se pueden formar con n dígitos.

        Args:
            n (int): Longitud de los números.
            expected_output (int|None): Valor esperado o None si solo se desea validar que se ejecuta correctamente.
        """
        result = self.solution.countGoodNumbers(n)

        if expected_output is not None:
            assert result == expected_output
        else:
            # Para casos sin valor esperado concreto, solo validamos que es un entero en el rango correcto
            assert isinstance(result, int)
            assert 0 <= result < 10**9 + 7
