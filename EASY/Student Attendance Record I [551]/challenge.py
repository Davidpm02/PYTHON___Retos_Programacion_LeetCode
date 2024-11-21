"""
DESCRIPTION:

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    'A': Absent.
    'L': Late.
    'P': Present.

The student is eligible for an attendance award if they meet both of the following criteria:

    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.

Return true if the student is eligible for an attendance award, or false otherwise.

 

Example 1:

  Input: s = "PPALLP"
  Output: true
  Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

Example 2:

  Input: s = "PPALLL"
  Output: false
  Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

 

Constraints:

    1 <= s.length <= 1000
    s[i] is either 'A', 'L', or 'P'.

"""

from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        
        """
        Comprueba si un alumno dado es merecedor de obtener un precio
        por de asistencia, dado el histórico de asintencia del mismo.

        params:
            - s (str) -- Cadena que representa el histórico de asistencia
            del alumno.
        returns:
            bool
        """

        chars_counter = Counter(s)
        if (chars_counter['A'] >= 2):
            return False
        
        consecutive_lates = 0
        for idx, _ in enumerate(s):
            if (_ == 'L'):
                consecutive_lates += 1
            else:
                consecutive_lates = 0
            if (consecutive_lates == 3):
                return False
        if (consecutive_lates == 3):
                return False
        return True

