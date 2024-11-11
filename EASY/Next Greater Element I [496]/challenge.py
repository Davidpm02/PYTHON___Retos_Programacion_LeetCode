"""
DESCRIPTION:

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

  Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
  Output: [-1,3,-1]
  Explanation: The next greater element for each value of nums1 is as follows:
   - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
   - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
   - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

  Input: nums1 = [2,4], nums2 = [1,2,3,4]
  Output: [3,-1]
  Explanation: The next greater element for each value of nums1 is as follows:
   - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
   - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

 

Constraints:

    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 104
    All integers in nums1 and nums2 are unique.
    All the integers of nums1 also appear in nums2.

"""

from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        """
        Summary:
            Método de la clase Solution encargado de generar un array donde cada 
            elemento corresponde al elemento mayor más cercano del elemento con
            el mismo índice en 'nums1'.

            En caso de no existir un elemento mayor para un entero dado,
            el array resultado contiene el valor -1.
        Args:
            nums1 (List[int])
            nums2 (List[int])
        Returns:
            result_array (List[int])
        """

        result_array = []
        for num in nums1:
            index_num_in_nums2 = nums2.index(num)
            try:
                limited_nums2 = nums2[index_num_in_nums2 + 1:]
                print('nums2 ==>', limited_nums2)
                for num2 in limited_nums2:
                    if (num2 > num):
                        result_array.append(num2)
                        break
                if (len(result_array) == len(nums1)):
                    return result_array
                result_array.append(-1)
            except:
                result_array.append(-1)
        return result_array