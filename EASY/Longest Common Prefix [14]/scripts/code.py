"""
DESCRIPTION:

## TODO ==> Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

  Input: strs = ["flower","flow","flight"]
  Output: "fl"


Example 2:

  Input: strs = ["dog","racecar","car"]
  Output: ""
  Explanation: There is no common prefix among the input strings.
 

Constraints:

  1 <= strs.length <= 200
  0 <= strs[i].length <= 200
  strs[i] consists of only lowercase English letters.

"""
from typing import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
      """Método de la clase Solution que procesa un array de elementos string, y retorna el prefijo más largo que
         esté presente en todas las cadenas del array.
         
         Args:
             strs -- Array de elementos string a procesar por la función.
        
         Returns:
             str -- Cadena con el prefijo más largo encontrado en todos los elementos del array 'strs'.
      """
      
      if any(len(string) == 0 for string in strs):
        return ""
      
      
      # Defino una lista con caracteres que se incluyan en todos los elementos del parámetro 'strs'
      common_chars = []
      strs_refer = strs.copy()
      # Itero sobre el array recibido como parámetro
      while True:
    
        index_1_chars = []
        for index, string in enumerate(strs_refer):
          try:
            index_1_chars.append(string[0])
          except IndexError:
            break
        print(index_1_chars)
        if (len(index_1_chars) == len(strs)) and len(set(index_1_chars)) == 1:
          try:
            common_chars.append(index_1_chars[0])
            strs_refer = [string[1:] for string in strs_refer]   # Actualizo la lista de referencia
            continue
          except IndexError:
            continue
        else:
          break
        
      
      # Construyo la cadena con el prefijo más largo encontrado
      longest_prefix = "".join(common_chars)
      return longest_prefix



if __name__ == "__main__":
  
  strs = ["ab", "a"]
  solution = Solution()
  sol = solution.longestCommonPrefix(strs=strs)
  print(sol)
      
        