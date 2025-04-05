import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una nueva instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("ababcbacadefegdehijhklij", [9, 7, 8]),   # Ejemplo clásico de partición óptima
            ("eccbbbbdec", [10]),                     # Todos los caracteres están conectados, por lo que es una sola partición
            ("abc", [1, 1, 1]),                        # Cada letra aparece una sola vez
            ("aaaaa", [5]),                            # Todos los caracteres son iguales
            ("abac", [3, 1]),                          # 'a' y 'b' aparecen dentro de la primera partición, 'c' va sola
            ("a", [1]),                                # Un solo carácter debe devolver una partición de longitud 1
            ("", []),                                  # Cadena vacía devuelve lista vacía
            ("caedbdedda", [1, 9]),                    # Varias apariciones que obligan a agrupar ciertas letras
        ]
    )
    def test_partition_labels(self, input_str, expected_output):
        """
        Valido la correcta partición de la cadena según las reglas del problema.

        Args:
            input_str (str): La cadena de entrada a particionar.
            expected_output (List[int]): Las longitudes esperadas de cada partición.
        """
        assert self.solution.partitionLabels(input_str) == expected_output
