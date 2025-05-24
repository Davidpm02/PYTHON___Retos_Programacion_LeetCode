import pytest
from challenge import Solution  # Asumo que el archivo se llama challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo instancia de Solution para ejecutar tests."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, edges, expected_output",
        [
            # Caso 1: árbol con 1 nodo (sin aristas)
            ([5], 2, [], 7),  # XOR(5,2) = 7, máximo es con XOR aplicado
            
            # Caso 2: árbol con 2 nodos, beneficio solo para nodo 0
            ([1, 4], 3, [[0, 1]], 6),  
            # explicación: nodo 0: 1^3=2 beneficio=2-1=1 >0; nodo1:4^3=7 beneficio=3 >0
            # pero con paridad debe seleccionar mejor suma
            
            # Caso 3: árbol con 3 nodos en línea, donde XOR no es beneficioso
            ([2, 2, 2], 0, [[0, 1], [1, 2]], 6),  # Sin cambio, suma total 6
            
            # Caso 4: árbol con 3 nodos en línea, XOR muy beneficioso
            ([1, 2, 3], 7, [[0, 1], [1, 2]], 18),
            # valores XOR: [6, 5, 4], y combinaciones suman máximo
            
            # Caso 5: árbol con forma de estrella, elegir nodo central para XOR
            ([10, 1, 1, 1], 5, [[0,1],[0,2],[0,3]], 28),
            # Nodo 0: 10^5=15 beneficio +5, otros no cambian mucho
            
            # Caso 6: árbol más complejo (5 nodos), k=4
            ([3, 6, 8, 2, 7], 4, [[0,1],[1,2],[1,3],[3,4]], 36),
            
            # Caso 7: árbol con todos beneficios negativos (usar no ayuda)
            ([1, 1, 1], 0, [[0, 1], [1, 2]], 3),
            
            # Caso 8: árbol con valores cero y k != 0
            ([0, 0, 0], 5, [[0,1],[1,2]], 10),  # XOR en todos es beneficioso
            
            # Caso 9: árbol con un nodo, k = 0 (sin cambio)
            ([7], 0, [], 7),
        ]
    )
    def test_maximum_value_sum(self, nums, k, edges, expected_output):
        """
        Test parametrizado para validar el método maximumValueSum en varios escenarios.

        Args:
            nums (List[int]): Valores iniciales en los nodos.
            k (int): Valor para aplicar XOR.
            edges (List[List[int]]): Lista de aristas que forman el árbol.
            expected_output (int): Resultado esperado para la suma máxima.
        """
        assert self.solution.maximumValueSum(nums, k, edges) == expected_output
