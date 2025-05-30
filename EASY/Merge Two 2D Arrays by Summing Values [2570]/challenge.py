"""
DESCRIPTION:

You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

 

Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
Example 2:

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
 

Constraints:

1 <= nums1.length, nums2.length <= 200
nums1[i].length == nums2[j].length == 2
1 <= idi, vali <= 1000
Both arrays contain unique ids.
Both arrays are in strictly ascending order by id.

"""

from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        """
        Se encarga de unificar los elementos de comunes y no comunes
        de dos arrays recibidos como parámetro, en un nuevo array
        que contenga todos los índices que se encuentran en ambos arrays
        y cuyos valores se sumen entre sí.

        params:
            nums1 (List[List[int]])
            nums2 (List[List[int]])
        
        returns:
            List[List[int]]
        """

        # Inicilizo un diccionario de mapeo de los elementos en ambos
        # arrays.
        elements_hashmap = dict()
        for element in nums1:
            if (element[0] not in elements_hashmap):
                elements_hashmap[element[0]] = element[1]
            else:
                elements_hashmap[element[0]] += element[1]
            
        for element in nums2:
            if (element[0] not in elements_hashmap):
                elements_hashmap[element[0]] = element[1]
            else:
                elements_hashmap[element[0]] += element[1]
        
        # Ordeno el diccionario y convierto agrego los pares en una lista.
        elements_hashmap = dict(sorted(elements_hashmap.items()))
        result_array = [[index, value] for index, value in elements_hashmap.items()]
        return result_array