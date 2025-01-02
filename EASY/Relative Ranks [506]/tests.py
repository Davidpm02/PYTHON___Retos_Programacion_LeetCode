import pytest
from challenge import Solution  # Asegúrate de que el archivo se llame challenge.py y la clase Solution esté definida allí.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "score, expected_output",
        [
            # Casos estándar con diferentes puntuaciones
            ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),  # Puntuaciones ordenadas de mayor a menor
            ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),  # Clasificación de diferentes puntuaciones

            # Caso con puntuaciones iguales
            ([3, 3, 3], ["Gold Medal", "Gold Medal", "Gold Medal"]),  # Todos tienen la misma puntuación, deben recibir medalla

            # Caso con un solo participante
            ([10], ["Gold Medal"]),  # Solo hay un participante, debería recibir "Gold Medal"

            # Caso con dos participantes
            ([10, 5], ["Gold Medal", "Silver Medal"]),  # Dos participantes, el primero gana la medalla de oro, el segundo la de plata

            # Caso con más de 3 participantes pero con pocos valores (probando con menos de 5)
            ([100, 99, 98, 97, 96], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),  # Tres medallas y los demás como números

            # Caso con todos los números iguales (se les dará "Gold Medal" a todos)
            ([7, 7, 7], ["Gold Medal", "Gold Medal", "Gold Medal"]),  # Todos los mismos puntajes
        ]
    )
    def test_findRelativeRanks(self, score, expected_output):
        """
        Prueba parametrizada para validar la función findRelativeRanks.

        Args:
            score (List[int]): La lista de puntuaciones a evaluar.
            expected_output (List[str]): La lista de clasificaciones esperadas para las puntuaciones.
        """
        assert self.solution.findRelativeRanks(score) == expected_output
