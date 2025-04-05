import pytest
from challenge import Solution, TreeNode


class TestSolution:
    def setup_method(self):
        """Inicializo una nueva instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "tree, expected_val",
        [
            # Árbol:      1
            #           /   \
            #          2     3
            #         /     / \
            #        4     5   6
            #                   \
            #                    7
            # Resultado esperado: 7 (única hoja más profunda)
            (
                TreeNode(1,
                    TreeNode(2,
                        TreeNode(4)
                    ),
                    TreeNode(3,
                        TreeNode(5),
                        TreeNode(6, None, TreeNode(7))
                    )
                ),
                7
            ),
            # Árbol:      1
            #           /   \
            #          2     3
            # Resultado esperado: 1 (2 y 3 están al mismo nivel)
            (
                TreeNode(1,
                    TreeNode(2),
                    TreeNode(3)
                ),
                1
            ),
            # Árbol:        1
            #              /
            #             2
            #            /
            #           3
            # Resultado esperado: 3 (única hoja más profunda)
            (
                TreeNode(1,
                    TreeNode(2,
                        TreeNode(3)
                    )
                ),
                3
            ),
            # Árbol vacío
            (
                None,
                None
            ),
            # Árbol con un solo nodo
            (
                TreeNode(42),
                42
            ),
            # Árbol:         1
            #              /   \
            #             2     3
            #            /     / \
            #           4     5   6
            #          /           \
            #         7             8
            # Resultado esperado: 1 (7 y 8 están al mismo nivel, pero en lados distintos)
            (
                TreeNode(1,
                    TreeNode(2,
                        TreeNode(4,
                            TreeNode(7)
                        )
                    ),
                    TreeNode(3,
                        TreeNode(5),
                        TreeNode(6,
                            None,
                            TreeNode(8)
                        )
                    )
                ),
                1
            ),
        ]
    )
    def test_lca_deepest_leaves(self, tree, expected_val):
        """
        Valido la funcionalidad del método lcaDeepestLeaves en diferentes estructuras de árbol.

        Args:
            tree (TreeNode): La raíz del árbol a evaluar.
            expected_val (int or None): El valor del nodo que debería ser el LCA.
        """
        result_node = self.solution.lcaDeepestLeaves(tree)
        if result_node is None:
            assert expected_val is None
        else:
            assert result_node.val == expected_val
