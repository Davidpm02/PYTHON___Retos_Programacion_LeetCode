import pytest
from challenge import Solution  # Asegúrate de que el archivo challenge.py contiene la clase Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "numCourses, prerequisites, queries, expected_output",
        [
            (2, [[1, 0]], [[0, 1], [1, 0]], [False, True]),  # Caso donde el curso 0 no es prerrequisito de 1, pero 1 es prerrequisito de 0
            (2, [], [[1, 0], [0, 1]], [False, False]),      # Caso sin prerrequisitos, todos los cursos son independientes
            (3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]], [True, True]),  # Los cursos están conectados como 1 -> 2 -> 0
            (4, [[0, 1], [1, 2], [2, 3]], [[0, 3], [3, 0]], [True, False]),  # Secuencia de prerrequisitos lineales
            (5, [[0, 1], [2, 1], [3, 2], [4, 3]], [[0, 4], [1, 2], [3, 4]], [True, True, False]),  # Verificación con múltiples consultas
            (3, [[0, 1]], [[1, 2], [0, 2]], [False, False]),  # Ningún curso es prerrequisito de otro en este caso
        ]
    )
    def test_check_if_prerequisite(self, numCourses, prerequisites, queries, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método checkIfPrerequisite.

        Args:
            numCourses (int): Número de cursos disponibles.
            prerequisites (List[List[int]]): Lista de prerrequisitos para los cursos.
            queries (List[List[int]]): Consultas sobre si un curso es prerrequisito de otro.
            expected_output (List[bool]): Resultados esperados para las consultas.
        """
        assert self.solution.checkIfPrerequisite(numCourses, prerequisites, queries) == expected_output
