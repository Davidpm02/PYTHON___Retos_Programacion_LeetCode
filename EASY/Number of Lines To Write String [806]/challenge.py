"""
DESCRIPTION:

You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:

    result[0] is the total number of lines.
    result[1] is the width of the last line in pixels.

 

Example 1:

Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.

Example 2:

Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
Output: [2,4]
Explanation: You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.

 

Constraints:

    widths.length == 26
    2 <= widths[i] <= 10
    1 <= s.length <= 1000
    s contains only lowercase English letters.

"""

from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        """
        Se encarga de devolver el total de líneas que ocuparía escribir
        la cadena 's', dado el ancho en píxeles de cada carácter del
        alfabeto Inglés dentro de 'widths'.

        El resultado se compone de una lista de dos elementos, donde
        result[0] representa el total de líneas escritas, y result[1]
        el ancho en píxeles de la última línea escrita.

        params:
            widths (List[int])
            s (str)
        
        returns:
            List[int]
        """

        english_abc_array = [chr(_) for _ in range(97, 97 + 26)]
        width_per_letter_dict = dict(zip(english_abc_array, widths))

        # Inicializo la lista resultado
        result = [1, 0]
        while True:
            line_width = 0
            for idx, char in enumerate(s):
                if ((line_width + width_per_letter_dict[char]) < 100):
                    line_width += width_per_letter_dict[char]
                    continue
                elif ((line_width + width_per_letter_dict[char]) == 100):
                    line_width += width_per_letter_dict[char]
                    s = s[idx + 1:]
                    if (len(s) > 0):
                        result[0] += 1
                        break
                    else:
                        result[1] = line_width if (line_width != 0) else 100
                        return result
                else:
                    result[0] += 1
                    s = s[idx:]
                    break
            else:
                result[1] = line_width if (line_width != 0) else 100
                return result
