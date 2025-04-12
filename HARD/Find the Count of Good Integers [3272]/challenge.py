"""
DESCRIPTION:

You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a palindrome.
x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

551 because it can be rearranged to form 515.
525 because it is already k-palindromic.
Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468

 

Constraints:

1 <= n <= 10
1 <= k <= 9

"""

from math import factorial
from itertools import product

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        """
        Se encarga de contar cuántos enteros de n dígitos (sin ceros 
        iniciales) pueden reordenarse para formar un entero 
        palindrómico divisible por k.

        Un entero es considerado "good" si alguna de sus permutaciones
        forma un palíndromo divisible por k.
        
        params:
            n (int)
            k (int)

        returns:
            int
        """

        # Set para almacenar los multiconjuntos (frecuencias de dígitos) de palíndromos válidos
        good_multisets = set()
        
        # Función auxiliar para obtener la tupla de frecuencias de dígitos de un string numérico
        def get_freq(num_str: str):
            freq = [0] * 10
            for ch in num_str:
                freq[int(ch)] += 1
            return tuple(freq)
        
        # Genero palíndromos según si n es par o impar.
        if n % 2 == 0:
            half_len = n // 2
            # Uso product para generar todas las posibles mitades
            for half in product(range(10), repeat=half_len):
                # Evito que el palíndromo tenga un cero al comienzo
                if half[0] == 0:
                    continue
                left = ''.join(str(d) for d in half)
                # El palíndromo se forma concatenando la mitad invertida
                right = left[::-1]
                num_str = left + right
                num = int(num_str)
                # Compruebo divisibilidad entre k
                if num % k == 0:
                    # Registro el multiconjunto de dígitos
                    good_multisets.add(get_freq(num_str))
        else:
            half_len = n // 2
            for half in product(range(10), repeat=half_len):
                if half_len > 0 and half[0] == 0:
                    continue
                left = ''.join(str(d) for d in half)
                for mid in range(10):
                    # Construyo el número palindrómico con dígito central
                    num_str = left + str(mid) + left[::-1]
                    num = int(num_str)
                    if num % k == 0:
                        good_multisets.add(get_freq(num_str))
        
        # Ahora, calculo la cantidad de números con n dígitos para cada multiconjunto válido
        res = 0
        for freq in good_multisets:
            # Calculo las permutaciones totales de n dígitos con la fórmula de multiconjunto
            total = factorial(n)
            for f in freq:
                total //= factorial(f)
            
            # Calculo cuántos de esos números tendrían un cero inicial (no válidos)
            invalid = 0
            if freq[0] > 0:
                # Resto que al fijar 0 en la primera posición, se reduce la cuenta de dígitos del 0 en 1
                invalid = factorial(n - 1)
                invalid //= factorial(freq[0] - 1)
                for d in range(1, 10):
                    invalid //= factorial(freq[d])
            
            valid = total - invalid
            res += valid
        
        return res