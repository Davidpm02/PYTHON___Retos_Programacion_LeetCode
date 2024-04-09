"""
DESCRIPTION:

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

## TODO
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 

Example 1:

  Input: s = "PAYPALISHIRING", numRows = 3
  Output: "PAHNAPLSIIGYIR"


Example 2:

  Input: s = "PAYPALISHIRING", numRows = 4
  Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


Example 3:

  Input: s = "A", numRows = 1
  Output: "A"
 

## Constraints:

  1 <= s.length <= 1000
  s consists of English letters (lower-case and upper-case), ',' and '.'.
  1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        """
          Summary:
            Función parametrizada que recibe una cadena como parámetro de entrada, y, en base al valor del parámetro 'numRows',
            devuelve una nueva cadena, la cual corresponde a la lectura de la cadena de entrada, dispuesta a modo de zigzag.
          
          Args:
            s -- Cadena de entrada a ser procesada por la función.
            numRows -- Entero que corresponde al número de filas que debe tener la estructura zigzag generada a partir de la cadena
                       de entrada 's'.
          
          Returns:
            str -- Cadena de texto que se forma al leer, fila a fila, los caracteres del parámetro 's', dispuestos en estructura de 
                   zigzag, con un número de filas 'numRows'.
        """
        
        # Defino una lista con los caracteres del parámetro 's'
        characters_array = [char for char in s]
        
        
        ## LÓGICA
        
        # Defino un array padre, que contendrá los diferentes arrays que vaya creando
        zigzag_matrix = []
        
        # Instancio una referencia del indice del carácter sobre el que itero
        index = 0
        # Otras referencias para arrays intermedios
        n_non_ceros_in_middle_arrays = numRows - 2
        actual_position_in_n_non_ceros = 1
        
        while index < len(characters_array):
          # Itero sobre los caracteres del array
          for i, char in enumerate(characters_array):
              if len(zigzag_matrix) == 0:
                  matrix_col = [char for char in characters_array[:numRows]]
                  zigzag_matrix.append(matrix_col)
                  index = numRows
                  if index >= len(characters_array):
                      break
                  continue
              else:
                  if actual_position_in_n_non_ceros > n_non_ceros_in_middle_arrays:
                      if numRows == 3 and (0 not in zigzag_matrix[-1]):
                          # En este caso, es cierto que 'actual_position_in_n_non_ceros' siempre es igual a 'actual_position_in_n_non_ceros'
                          matrix_col = [0 for _ in range(numRows)]
                          matrix_col[actual_position_in_n_non_ceros] = characters_array[index]
                          zigzag_matrix.append(matrix_col[::-1])
                          index += 1
                          continue
            
                      matrix_col = [char for char in characters_array[index:(index + numRows)]]
                      zigzag_matrix.append(matrix_col)
                      index += numRows
                      actual_position_in_n_non_ceros = 1
                      if index >= len(characters_array):
                          break
                      continue
                  else:
                      if 0 not in zigzag_matrix[-1]:
                          matrix_col = [0 for _ in range(numRows)]
                          matrix_col[actual_position_in_n_non_ceros] = characters_array[index]
                          zigzag_matrix.append(matrix_col[::-1])
                          actual_position_in_n_non_ceros +=1
                          index += 1
                          if index >= len(characters_array):
                              break
                          continue
                      
                      else:  
                          last_col = zigzag_matrix[-1]
                          if last_col[actual_position_in_n_non_ceros + 1] == 0:
                              matrix_col = [0 for _ in range(numRows)]
                              matrix_col[actual_position_in_n_non_ceros] = characters_array[index]
                              zigzag_matrix.append(matrix_col[::-1])
                              actual_position_in_n_non_ceros +=1
                              index += 1
                              if index >= len(characters_array):
                                  break
                              continue
                          elif last_col[actual_position_in_n_non_ceros] == 0:
                              matrix_col = [0 for _ in range(numRows)]
                              matrix_col[actual_position_in_n_non_ceros] = characters_array[index]
                              zigzag_matrix.append(matrix_col[::-1])
                              actual_position_in_n_non_ceros +=1
                              index += 1
                              if index >= len(characters_array):
                                  break
                              continue
                              
          break
        print(zigzag_matrix)                
        
        ## Creando la cadena final
        final_str_characters_array = []
        index_char = 0
        while len(final_str_characters_array) < len(characters_array):
            for col_array in zigzag_matrix:
                col_array == col_array[::-1]

                if index_char == len(col_array):
                  break
                try:
                    if col_array[index_char] != 0:
                      final_str_characters_array.append(col_array[index_char])
                except IndexError:
                  break
        
            index_char +=1
        final_str = "".join(final_str_characters_array)
        return final_str

if __name__ == "__main__":
  
  s = "PAYPALISHIRING"

  numRows = 6
  solution = Solution()
  sol = solution.convert(s=s, 
                         numRows=numRows)
  
  print(sol)
                
                
             