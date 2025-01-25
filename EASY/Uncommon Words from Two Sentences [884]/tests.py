import pytest
from challenge import Solution  # Importa la clase Solution desde el archivo challenge.py (asumiendo que ese es el nombre del archivo del reto)

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s1, s2, expected_output",
        [
            ("apple orange banana", "banana grape fruit", ["apple", "orange", "grape", "fruit"]),  # Palabras únicas de ambas cadenas
            ("hello world hello", "world python java", ["python", "java"]),                         # Palabras únicas en la segunda cadena
            ("", "", []),                                                                             # Cadenas vacías (sin palabras)
            ("dog cat cat", "fish bird dog", ["fish", "bird"]),                                      # Palabras únicas en la segunda cadena
            ("apple apple", "banana banana", ["banana"]),                                            # Palabras únicas de la segunda cadena
            ("test only one", "test only one", []),                                                   # Sin palabras únicas
            ("zebra lion", "lion tiger tiger", ["zebra", "tiger"])                                  # Una palabra única en cada cadena
        ]
    )
    def test_uncommon_from_sentences(self, s1, s2, expected_output):
        """
        Prueba parametrizada para validar el funcionamiento de uncommonFromSentences.

        Args:
            s1 (str): La primera cadena de texto.
            s2 (str): La segunda cadena de texto.
            expected_output (List[str]): La lista de palabras esperadas que aparecen solo una vez.
        """
        assert self.solution.uncommonFromSentences(s1, s2) == expected_output
