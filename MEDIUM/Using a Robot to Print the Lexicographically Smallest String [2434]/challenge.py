"""
DESCRIPTION:

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 

Constraints:

1 <= s.length <= 10^5
s consists of only English lowercase letters.

"""

class Solution:
    def robotWithString(self, s: str) -> str:
        """
        Se encarga de construir la cadena lexicográficamente más pequeña
        posible en una salida `p`.

        Para ello, el método simula dos operaciones:
        1. Mover el primer carácter de `s` a un string temporal `t`
           (como si fuera una pila).
        2. Mover el último carácter de `t` a una salida `p` si ese
           carácter es el menor posible considerando los caracteres 
           restantes en `s`.

        params:
            s (str)
        
        returns:
            str
        """
        
        # Inicializo un arreglo que almacenará el menor carácter en s[i:]
        min_suffix = [''] * len(s)
        min_char = 'z'
        
        # Relleno el array con el menor carácter desde la posición i hasta el final
        for i in reversed(range(len(s))):
            min_char = min(min_char, s[i])
            min_suffix[i] = min_char

        t = []      # pila temporal
        res = []    # resultado final (lo escrito en el papel)
        i = 0       # índice para recorrer `s`

        while i < len(s) or t:
            # Mientras queden caracteres en `s`, empujo a `t`
            if i < len(s):
                t.append(s[i])  # paso el carácter actual a `t`
                i += 1

            # Mientras pueda escribir caracteres en orden correcto desde `t`
            while t and (i == len(s) or t[-1] <= min_suffix[i]):
                res.append(t.pop())  # escribo el último carácter de `t` en `res`

        return ''.join(res)
