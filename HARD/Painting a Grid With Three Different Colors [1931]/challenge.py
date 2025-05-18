"""
DESCRIPTION:

You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000

"""

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Calcula el número de formas de pintar una cuadrícula m x n usando
        3 colores (rojo, verde, azul), de forma que no haya dos celdas
        adyacentes (ni en filas ni en columnas) con el mismo color.

        params:
            m (int)
            n (int)

        returns:
            int

        """
        from functools import lru_cache
        MOD = 10**9 + 7
        COLORS = [0, 1, 2]  # 0: rojo, 1: verde, 2: azul

        # Genero todos los patrones válidos para una columna de altura m
        def generate_valid_columns():
            valid = []

            def backtrack(path):
                if len(path) == m:
                    valid.append(tuple(path))
                    return
                for color in COLORS:
                    if not path or path[-1] != color:
                        backtrack(path + [color])

            backtrack([])
            return valid

        valid_columns = generate_valid_columns()

        # Para cada patrón de columna, precomputo los patrones compatibles siguientes
        adjacency = {}
        for c1 in valid_columns:
            adjacency[c1] = []
            for c2 in valid_columns:
                if all(a != b for a, b in zip(c1, c2)):
                    adjacency[c1].append(c2)

        @lru_cache(None)
        def dp(col: int, prev_col_pattern: tuple) -> int:
            # Si hemos completado todas las columnas, hay una forma válida
            if col == n:
                return 1

            total = 0
            for next_col_pattern in adjacency[prev_col_pattern]:
                total = (total + dp(col + 1, next_col_pattern)) % MOD
            return total

        # Casos base: en la primera columna puedo colocar cualquier patrón válido
        result = 0
        for first_col in valid_columns:
            result = (result + dp(1, first_col)) % MOD

        return result
