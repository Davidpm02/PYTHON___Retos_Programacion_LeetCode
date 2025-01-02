import pytest
import pandas as pd
from challenge import not_boring_movies  # Ajusta el nombre del archivo o módulo según corresponda

class TestSolution:
    @pytest.mark.parametrize(
        "cinema, expected_output",
        [
            # Caso con varios registros y algunas películas con id impar y descripción diferente a 'boring'
            (
                pd.DataFrame({
                    'id': [1, 2, 3, 4],
                    'title': ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4'],
                    'description': ['exciting', 'boring', 'thrilling', 'boring'],
                    'rating': [8.5, 5.0, 9.0, 7.5]
                }),
                pd.DataFrame({
                    'id': [3, 1],
                    'title': ['Movie 3', 'Movie 1'],
                    'description': ['thrilling', 'exciting'],
                    'rating': [9.0, 8.5]
                }).sort_values('rating', ascending=False)
            ),
            # Caso donde no hay ninguna película con 'boring' o con un id impar
            (
                pd.DataFrame({
                    'id': [2, 4, 6],
                    'title': ['Movie 2', 'Movie 4', 'Movie 6'],
                    'description': ['thrilling', 'adventurous', 'exciting'],
                    'rating': [8.0, 7.2, 9.3]
                }),
                pd.DataFrame(columns=['id', 'title', 'description', 'rating'])
            ),
            # Caso donde todos los id son pares (no se debe devolver ningún registro)
            (
                pd.DataFrame({
                    'id': [2, 4, 6],
                    'title': ['Movie 2', 'Movie 4', 'Movie 6'],
                    'description': ['boring', 'boring', 'boring'],
                    'rating': [5.2, 3.4, 6.8]
                }),
                pd.DataFrame(columns=['id', 'title', 'description', 'rating'])
            ),
            # Caso donde todos los id son impares, pero la descripción es "boring" (ninguna película se devuelve)
            (
                pd.DataFrame({
                    'id': [1, 3, 5],
                    'title': ['Movie 1', 'Movie 3', 'Movie 5'],
                    'description': ['boring', 'boring', 'boring'],
                    'rating': [7.8, 6.2, 8.0]
                }),
                pd.DataFrame(columns=['id', 'title', 'description', 'rating'])
            ),
            # Caso con una sola película válida
            (
                pd.DataFrame({
                    'id': [1],
                    'title': ['Valid Movie'],
                    'description': ['exciting'],
                    'rating': [9.1]
                }),
                pd.DataFrame({
                    'id': [1],
                    'title': ['Valid Movie'],
                    'description': ['exciting'],
                    'rating': [9.1]
                })
            ),
            # Caso donde hay varias películas con 'boring' en la descripción, todas eliminadas
            (
                pd.DataFrame({
                    'id': [1, 2, 3],
                    'title': ['Movie 1', 'Movie 2', 'Movie 3'],
                    'description': ['boring', 'boring', 'boring'],
                    'rating': [7.5, 6.8, 9.2]
                }),
                pd.DataFrame(columns=['id', 'title', 'description', 'rating'])
            )
        ]
    )
    def test_not_boring_movies(self, cinema, expected_output):
        """
        Prueba parametrizada para validar la función not_boring_movies.
        
        Args:
            cinema (pd.DataFrame): El DataFrame de películas de entrada.
            expected_output (pd.DataFrame): El DataFrame esperado de salida.
        """
        result = not_boring_movies(cinema)
        
        # Comprobamos si los DataFrames son iguales
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_output.reset_index(drop=True))
