"""
DESCRIPTION:

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

    If locked[i] is '1', you cannot change s[i].
    But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:

Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.

Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.

 

Constraints:

    n == s.length == locked.length
    1 <= n <= 105
    s[i] is either '(' or ')'.
    locked[i] is either '0' or '1'.

"""

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        """
        Se encarga de verificar si una cadena puede actualizarse para
        formar una estructura de paréntesis válida, en función de los
        bloqueos de caracteres que se indiquen en el parámetro 'locked'.

        params:
            s (str)
            locked (str)
        
        returns:
            bool
        """

        n = len(s)
        
        # Si la longitud es impar, no puede ser válida
        if n % 2 != 0:
            return False
        
        # Primera pasada: de izquierda a derecha
        open_count = 0
        for i in range(n):
            if s[i] == '(' or (locked[i] == '0' and open_count < n // 2):
                open_count += 1
            elif s[i] == ')':
                open_count -= 1
            
            # Si el número de paréntesis abiertos es negativo en cualquier momento, no es válido
            if open_count < 0:
                return False

        # Segunda pasada: de derecha a izquierda
        close_count = 0
        for i in range(n-1, -1, -1):
            if s[i] == ')' or (locked[i] == '0' and close_count < n // 2):
                close_count += 1
            elif s[i] == '(':
                close_count -= 1
            
            # Si el número de paréntesis cerrados es negativo en cualquier momento, no es válido
            if close_count < 0:
                return False
        
        return True