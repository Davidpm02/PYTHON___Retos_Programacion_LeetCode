"""
DESCRIPTION:

Given an integer x, return true if x is a 
palindrome, and false otherwise.

 
Example 1:

  Input: x = 121
  Output: true
  Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:

  Input: x = -121
  Output: false
  Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

  Input: x = 10
  Output: false
  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

## Constraints:

  -231 <= x <= 231 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        """Método de la clase Solution que se encarga de verificar si un entero dado, recibido como parámetro,
           es un palíndromo o no.
           
           Args:
               x -- Entero comprendido en el rango [-2e31, 2e31-1] que se quiere evaluar.
            
           Returns:
               bool -- Booleano que determina si el entero recibido como parámetro es un palíndromo
                       o no.
        """
        
        ## LÓGICA
        
        return True if str(x)[::-1] == str(x) else False
      
      
if __name__ == "__main__":
  
  x = -121
  solution = Solution()
  sol = solution.isPalindrome(x=x)
  print(sol)
        
        
        