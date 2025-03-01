import pytest
from challenge import Solution, TreeNode

def tree_to_list(root):
    """
    Convierte un árbol binario en una lista representando su recorrido en preorden
    para facilitar la comparación en las pruebas.
    """
    if not root:
        return []
    return [root.val] + tree_to_list(root.left) + tree_to_list(root.right)

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "preorder, postorder, expected_preorder",
        [
            ([1], [1], [1]),  # Árbol con un solo nodo
            ([1, 2, 3], [3, 2, 1], [1, 2, 3]),  # Árbol lineal (sólo hijos izquierdos)
            ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], [1, 2, 4, 5, 3, 6, 7]),  # Árbol completo
            ([2, 1, 3], [1, 3, 2], [2, 1, 3]),  # Árbol con tres nodos balanceado
            ([1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4])  # Árbol degenerado (sólo hijos derechos)
        ]
    )
    def test_constructFromPrePost(self, preorder, postorder, expected_preorder):
        """
        Prueba parametrizada para validar la construcción del árbol a partir de
        listas de preorden y postorden.
        """
        root = self.solution.constructFromPrePost(preorder, postorder)
        assert tree_to_list(root) == expected_preorder
