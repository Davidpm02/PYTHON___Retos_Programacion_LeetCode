"""
DESCRIPTION:

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

 

Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".

 

Constraints:

    1 <= s.length <= 100
    s consists only of lowercase English letters and digits.
    The input is generated such that it is possible to delete all digits.

"""

class Solution:
    def clearDigits(self, s: str) -> str:
        

        """
        Se encarga de procesar una cadena de texto y eliminar todos los
        caracteres que sean dígitos, además del caracter más cercano a
        este situado a la izquierda.

        params:
            s (str)
        
        returns:
            str
        """

        idx_marked = {idx:1 if char in '0123456789' else 0 for idx, char in enumerate(s)}

        while (1 in list(idx_marked.values())):
            for idx, is_marked in idx_marked.items():
                if (is_marked == 1):
                    del idx_marked[idx]
                    for i in reversed(range(0, idx)):
                        if (i in idx_marked):
                            del idx_marked[i]
                            break
                        continue
                    break

        valid_chars = [char for idx, char in enumerate(s) if (idx in idx_marked)]
        return "".join(valid_chars)