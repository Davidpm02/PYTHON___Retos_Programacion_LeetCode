from ..scripts.code import *

def test_isPalindrome():
    # Testing positive integers
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(12321) == True
    assert Solution().isPalindrome(9009) == True
    
    # Testing negative integers
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(-9009) == False
    
    # Testing single-digit integers
    assert Solution().isPalindrome(5) == True
    assert Solution().isPalindrome(-5) == False
    
    # Testing zero
    assert Solution().isPalindrome(0) == True
    
    # Testing boundary conditions
    assert Solution().isPalindrome(2147447412) == True
    assert Solution().isPalindrome(-2147483648) == False


test_isPalindrome()