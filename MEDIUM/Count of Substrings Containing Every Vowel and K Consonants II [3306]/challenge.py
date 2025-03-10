"""
DESCRIPTION:

You are given a string word and a non-negative integer k.

Return the total number of

of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

    word[0..5], which is "ieaouq".
    word[6..11], which is "qieaou".
    word[7..12], which is "ieaouq".

 

Constraints:

    5 <= word.length <= 2 * 105
    word consists only of lowercase English letters.
    0 <= k <= word.length - 5

"""

from bisect import bisect_right
from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        """
        Se encarga de hallar el total de subcadenas de 'word' que
        contienen todas las vocales ['a', 'e', 'i', 'o', 'u'] al
        menos una vez, y un número exacto de 'k' consonantes.

        params:
            word (str)
            k (int)
        
        returns:
            int
        """

        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        
        # Precalculo de prefix sum para consonantes.
        prefix_cons = [0] * (n + 1)
        for i in range(1, n + 1):
            # Incremento el contador si el caracter no es vocal.
            prefix_cons[i] = prefix_cons[i-1] + (0 if word[i-1] in vowels else 1)
        
        # Para cada posible valor de prefix_cons, almaceno los índices en una lista ordenada.
        pos_by_prefix = defaultdict(list)
        for i, cnt in enumerate(prefix_cons):
            pos_by_prefix[cnt].append(i)
        
        # Inicializo el diccionario para guardar el último índice de cada vocal
        last_occurrence = {v: -1 for v in vowels}
        
        result = 0
        # Recorro cada posición final r de la subcadena
        for r in range(n):
            char = word[r]
            if char in vowels:
                # Actualizo el último índice donde apareció la vocal.
                last_occurrence[char] = r
            
            # Verifico si ya he visto todas las vocales al menos una vez.
            if min(last_occurrence.values()) == -1:
                continue  # No puedo formar una subcadena válida aún.
            
            # Para que la subcadena [l, r] tenga todas las vocales, l debe ser <= l_max,
            # donde l_max es el mínimo de los últimos índices de aparición de cada vocal.
            l_max = min(last_occurrence.values())
            
            # Calculo el valor target para la suma de consonantes en el prefix: 
            # Necesito que prefix_cons[r+1] - prefix_cons[l] == k  =>  prefix_cons[l] == prefix_cons[r+1] - k
            target = prefix_cons[r+1] - k
            
            # Verifico que existan índices con ese valor target.
            if target in pos_by_prefix:
                # Uso binary search para contar cuántos índices l en pos_by_prefix[target]
                # son <= l_max.
                count = bisect_right(pos_by_prefix[target], l_max)
                result += count

        return result
