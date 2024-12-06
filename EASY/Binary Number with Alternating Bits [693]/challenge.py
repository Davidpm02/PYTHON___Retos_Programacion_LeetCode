"""
DESCRIPTION:

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

  Input: n = 5
  Output: true
  Explanation: The binary representation of 5 is: 101

Example 2:

  Input: n = 7
  Output: false
  Explanation: The binary representation of 7 is: 111.

Example 3:

  Input: n = 11
  Output: false
  Explanation: The binary representation of 11 is: 1011.


Constraints:

    1 <= n <= 231 - 1

"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        """
        Comprueba si la representación en binario para un
        entero dado está compuesta, en su totalidad, por bits
        alternantes.

        params:
            n (int)
        
        returns:
            bool
        """

        for idx, bit in enumerate(str(bin(n))):
            try:
                if (idx != 0):
                    assert (bit != str(bin(n))[idx - 1])
            except AssertionError:
                return False
        return True