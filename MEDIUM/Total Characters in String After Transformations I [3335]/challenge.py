"""
DESCRIPTION:

You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
 

Constraints:

1 <= s.length <= 10^5
s consists only of lowercase English letters.
1 <= t <= 10^5

"""

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        Calcula la longitud de una cadena después de aplicar t transformaciones.
        
        En cada transformación:
        - Si el carácter es 'z', se reemplaza por "ab"
        - De lo contrario, se reemplaza por la siguiente letra del alfabeto
        
        La implementación mantiene las frecuencias de cada carácter y las actualiza
        en cada transformación, lo que permite calcular eficientemente la longitud
        final incluso para valores grandes de t.
        
        Args:
            s: Una cadena de caracteres en minúscula
            t: Número de transformaciones a aplicar
            
        Returns:
            La longitud de la cadena resultante después de t transformaciones,
            módulo 10^9 + 7
        """
        MOD = 10**9 + 7
        
        # Inicializamos el recuento de frecuencias para cada carácter
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # Aplicamos las t transformaciones
        for _ in range(t):
            new_freq = [0] * 26
            
            # Procesamos cada carácter excepto 'z'
            for i in range(25):  # a hasta y
                new_freq[i + 1] += freq[i]  # Cada carácter se convierte en el siguiente
            
            # Procesamos 'z' por separado (se convierte en "ab")
            new_freq[0] += freq[25]  # 'z' -> 'a'
            new_freq[1] += freq[25]  # 'z' -> 'b'
            
            freq = new_freq
        
        # Calculamos la longitud total sumando todas las frecuencias
        total_length = sum(freq) % MOD
        
        return total_length