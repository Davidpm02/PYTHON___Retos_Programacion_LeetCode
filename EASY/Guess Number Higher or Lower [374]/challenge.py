"""
DESCRIPTION:

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

 

Example 1:

  Input: n = 10, pick = 6
  Output: 6

Example 2:

  Input: n = 1, pick = 1
  Output: 1

Example 3:

  Input: n = 2, pick = 1
  Output: 1

 

Constraints:

    1 <= n <= 231 - 1
    1 <= pick <= n

"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random
class Solution:
    def guessNumber(self, n: int) -> int:

        """
        """

        # Array de posibles números
        # Selecciono un número intermedio
        possible_nums = [num for num in range(1, n + 1)]
        selected_num = possible_nums[(len(possible_nums) // 2)]

        # Búsqueda binaria para adivinar el número seleccionado
        while True:
            if (guess(selected_num) == 0):
                return selected_num
            elif (guess(selected_num) == 1):
                index_selected_num = possible_nums.index(selected_num)
                possible_nums[:] = possible_nums[index_selected_num:]
                selected_num = possible_nums[(len(possible_nums) // 2)]
                continue
            elif (guess(selected_num) == -1):
                index_selected_num = possible_nums.index(selected_num)
                possible_nums[:] = possible_nums[:index_selected_num]
                selected_num = possible_nums[(len(possible_nums) // 2)]
                continue

        ## DEMASIADO LENTO PARA DARSE POR SOLUCIÓN VÁLIDA