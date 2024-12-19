"""
DESCRIPTION:

We have two special characters:

    The first character can be represented by one bit 0.
    The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

  Input: bits = [1,0,0]
  Output: true
  Explanation: The only way to decode it is two-bit character and one-bit character.
  So the last character is one-bit character.

Example 2:

  Input: bits = [1,1,1,0]
  Output: false
  Explanation: The only way to decode it is two-bit character and two-bit character.
  So the last character is not one-bit character.

 

Constraints:

    1 <= bits.length <= 1000
    bits[i] is either 0 or 1.

"""

from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        """
        Dada las condiciones del reto, se encarga de verificar
        si el último carácter de 'bits' debe ser un carácter de
        un único bit.

        params:
            bits (List[int])
        
        returns:
            bool
        """

        original_bits = bits.copy()
        if (len(bits) == 1):
            # El único elemento es 0; se retorna True
            return True

        idx_counter = 0
        while True:
            for bit in bits:
                if (len(bits) == 1):
                    # El único elemento es 0; se retorna True
                    return True
                        
                if (bit == 0):
                    idx_counter +=1
                    bits = original_bits[idx_counter:]
                    break
                else:
                    idx_counter +=2
                    bits = original_bits[idx_counter:]
                    break
            if (len(bits) > 0):
                continue
            else:
                return False
