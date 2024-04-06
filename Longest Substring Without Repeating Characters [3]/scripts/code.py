"""
DESCRIPTION:

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string `s`, this function returns the length of the longest substring without repeating characters.
        """
        
        # Uso una ventana de slicing para buscar la subcadena más larga
        window = {}
        max_length = 0  # Referencia a la longitud máxima encontrada
        start = 0  
        
        for i, char in enumerate(s):
            if char in window:
                start = max(start, window[char] + 1)
            window[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length   # Si len(s) == 0, ==> max_length = 0
            
        
        
    
    def validateString(self, s):
        
        """
        Validate a given string.
        
        Parameters:
            self (obj): The object instance.
            s (str): The string to be validated.
        
        Returns:
            None
        """
        
        assert len(s) >= 0 and len(s) <= (5*104)
        
        
if __name__ == "__main__":
    
    s = ""
    solution = Solution()
    sol = solution.lengthOfLongestSubstring(s)
    
    print(sol)