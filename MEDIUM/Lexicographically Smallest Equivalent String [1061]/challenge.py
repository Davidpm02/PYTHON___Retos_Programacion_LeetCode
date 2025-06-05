"""
DESCRIPTION:

You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

 

Example 1:

Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
Example 2:

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
Example 3:

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
 

Constraints:

1 <= s1.length, s2.length, baseStr <= 1000
s1.length == s2.length
s1, s2, and baseStr consist of lowercase English letters.

"""

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Dado s1, s2 con la misma longitud y baseStr, construye la cadena equivalente
        lexicográficamente más pequeña usando la información de equivalencia entre caracteres.
        """
        # Inicializo el arreglo parent para cada letra 'a' a 'z'.
        parent = [i for i in range(26)]

        def find(x: int) -> int:
            # Encuentro el representante (raíz) de x con path compression.
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            # Uno los conjuntos de x e y. Mantengo como raíz el carácter menor.
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return
            if rx < ry:
                parent[ry] = rx
            else:
                parent[rx] = ry

        # Recorro todas las parejas de s1 y s2 para unir sus equivalencias.
        for c1, c2 in zip(s1, s2):
            idx1 = ord(c1) - ord('a')
            idx2 = ord(c2) - ord('a')
            union(idx1, idx2)

        # Construyo el resultado reemplazando cada carácter por su representante mínimo.
        resultado = []
        for c in baseStr:
            idx = ord(c) - ord('a')
            rep = find(idx)
            # Convierto el índice de vuelta a carácter.
            resultado.append(chr(rep + ord('a')))

        return "".join(resultado)
