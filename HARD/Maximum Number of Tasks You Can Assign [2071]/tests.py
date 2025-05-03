import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "tasks, workers, pills, strength, expected_output",
        [
            ([3, 4, 5], [5, 6, 7], 1, 1, 3),          # Ejemplo básico con suficiente fuerza y píldoras
            ([10, 20, 30], [5, 10, 15], 1, 5, 2),     # Tareas más difíciles, 2 tareas completadas con 1 píldora
            ([1, 2, 3], [2, 3, 4], 0, 1, 3),          # Sin píldoras, pero todos los trabajadores son suficientemente fuertes
            ([5, 10, 15], [4, 8, 12], 1, 2, 2),       # 1 píldora, solo 2 tareas completadas
            ([10, 20, 30, 40], [10, 20, 30, 40], 1, 1, 3),  # Igual número de tareas y trabajadores
            ([1, 2], [3, 4], 0, 5, 2),                # Sin píldoras, pero fuerza suficiente
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 2, 1, 5),  # Con 2 píldoras, todas las tareas se pueden hacer
            ([10, 20, 30], [5, 6, 7], 0, 5, 2),       # Sin píldoras, solo 2 tareas completadas
            ([1], [2], 0, 5, 1),                      # Caso mínimo: 1 tarea y 1 trabajador
            ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1], 0, 5, 1),  # Todos los trabajadores con la misma fuerza
        ]
    )
    def test_max_task_assign(self, tasks, workers, pills, strength, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método maxTaskAssign.

        Args:
            tasks (List[int]): Lista de tareas con los valores de fuerza requeridos.
            workers (List[int]): Lista de trabajadores con las fuerzas disponibles.
            pills (int): Número de píldoras mágicas disponibles.
            strength (int): El valor que incrementa la fuerza de los trabajadores al usar una píldora.
            expected_output (int): El número esperado de tareas que se pueden completar.
        """
        assert self.solution.maxTaskAssign(tasks, workers, pills, strength) == expected_output
