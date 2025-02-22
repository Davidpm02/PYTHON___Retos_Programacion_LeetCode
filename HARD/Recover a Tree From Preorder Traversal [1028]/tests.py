import pytest
from challenge import Solution, TreeNode


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    def tree_to_list(self, root: TreeNode) -> list:
        """Convierte el árbol binario a una lista para facilitar la comparación."""
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Eliminar los None al final de la lista para evitar valores innecesarios
        while result and result[-1] is None:
            result.pop()
        return result

    @pytest.mark.parametrize(
        "traversal, expected_output",
        [
            ("1-2--3--4-5--6--7", [1, 2, 5, 3, 4, 6, 7]),  # Árbol típico con 7 nodos
            ("1-2--3---4-5--6---7", [1, 2, 5, 3, None, 6, None, 4, None, 7]),  # Árbol con nodos nulos
            ("1-401--349---90--88", [1, 401, None, 349, 88, 90]),  # Árbol con estructura variada
            ("1-2--3---4---5", [1, 2, None, 3, None, 4, None, 5]),  # Árbol con una rama izquierda
            ("1-2--3---4--5", [1, 2, None, 3, None, 4, None, 5]),  # Árbol con una rama izquierda
            ("1-2--3---4", [1, 2, None, 3, None, 4]),  # Árbol con nodos hasta profundidad 3
        ]
    )
    def test_recover_from_preorder(self, traversal, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función recoverFromPreorder.

        Args:
            traversal (str): La cadena que representa el recorrido en preorden.
            expected_output (list): El resultado esperado en forma de lista.
        """
        root = self.solution.recoverFromPreorder(traversal)
        tree_list = self.tree_to_list(root)
        assert tree_list == expected_output, f"Se esperaba {expected_output}, pero se obtuvo {tree_list}"
