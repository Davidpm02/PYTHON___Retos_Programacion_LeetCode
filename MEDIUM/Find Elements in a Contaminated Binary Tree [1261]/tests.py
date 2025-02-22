import pytest
from challenge import TreeNode, FindElements

class TestFindElements:
    def setup_method(self):
        """
        Método de configuración para inicializar diferentes estructuras de árbol
        antes de cada prueba.
        """
        # Árbol de prueba: 
        #         -1
        #        /   \
        #      -1    -1
        root = TreeNode()
        root.left = TreeNode()
        root.right = TreeNode()
        
        self.solution = FindElements(root)

    @pytest.mark.parametrize(
        "target, expected_output",
        [
            (0, True),  # La raíz siempre debe ser 0
            (1, True),  # Nodo izquierdo debe ser 1
            (2, True),  # Nodo derecho debe ser 2
            (3, False), # No está en el árbol
            (4, False), # No está en el árbol
        ]
    )
    def test_find(self, target, expected_output):
        """
        Prueba parametrizada para validar si un valor existe en el árbol recuperado.

        Args:
            target (int): El valor que se busca en el árbol.
            expected_output (bool): El resultado esperado de la búsqueda.
        """
        assert self.solution.find(target) == expected_output
