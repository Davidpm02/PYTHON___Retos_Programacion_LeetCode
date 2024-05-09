"""
DESCRIPTION:

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: 
[−231, 231 − 1].

For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1,
and if the quotient is strictly less than -231, then return -231.

 

Example 1:

  Input: dividend = 10, divisor = 3
  Output: 3
  Explanation: 10/3 = 3.33333.. which is truncated to 3.


Example 2:

  Input: dividend = 7, divisor = -3
  Output: -2
  Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

## Constraints:

  -2e31 <= dividend, divisor <= 2e31 - 1
  divisor != 0
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        """
        """
        
        if dividend == divisor:
            return 1
        elif dividend == -divisor:
            return -1



        times_divisor = 0
        if dividend < 0:
            new_dividend = -dividend
        else:
            new_dividend = dividend

        if divisor < 0:
            new_divisor = -divisor
        else:
            new_divisor = divisor
        
        if new_divisor == 1 or new_divisor == -1:
            times_divisor = new_dividend

            if (new_dividend < 0) and (new_divisor < 0):
                pass
            elif (new_dividend < 0) or (new_divisor < 0):
                times_divisor = -times_divisor 
            return times_divisor

        while new_dividend >= new_divisor:
          
          new_dividend -= new_divisor
          times_divisor += 1
        
        if (dividend < 0) and (divisor < 0):
          pass
        elif (dividend < 0) or (divisor < 0):
          times_divisor = -times_divisor
        
        if (times_divisor < -2**31):
          times_divisor = (-2**31)
        elif (times_divisor > (2**31 - 1)):
          times_divisor = (2**31 - 1)
        return times_divisor
      
      
if __name__ == "__main__":
  
  dividend = -2147483648
  divisor = -1
  solution = Solution()
  sol = solution.divide(dividend= dividend,
                        divisor= divisor)
  print(sol)