"""
DESCRIPTION:

You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.

 

Example 1:

Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
Output: 1
Explanation: 
There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
Example 2:

Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
Output: 4
Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
 

Constraints:

n == nums1.length == nums2.length
3 <= n <= 10^5
0 <= nums1[i], nums2[i] <= n - 1
nums1 and nums2 are permutations of [0, 1, ..., n - 1].

"""

from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        """
        Se encarga de contar el total de tripletes que pueden formase con
        los enteros de los arrays 'nums1' y 'nums2'.

        params:
            nums1 (List[int])
            nums2 (List[int])
        
        returns:
            int
        """

        n = len(nums1)
        
        # Mapeo de valores a posiciones en nums2
        pos2 = {}
        for i in range(n):
            pos2[nums2[i]] = i
        
        # Reordenar nums1 según las posiciones en nums2
        positions = [pos2[nums1[i]] for i in range(n)]
        
        # Implementación de BIT
        bit = [0] * (n + 1)
        
        def update(idx, val):
            idx += 1  # BIT es 1-indexado
            while idx <= n:
                bit[idx] += val
                idx += idx & -idx
        
        def query(idx):
            idx += 1  # BIT es 1-indexado
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res
        
        result = 0
        
        # Para cada valor en positions
        left = [0] * n
        for i in range(n):
            left[i] = query(positions[i])
            update(positions[i], 1)
        
        # Reiniciar BIT
        bit = [0] * (n + 1)
        
        # Recorrer posiciones en orden inverso para calcular 'right'
        for i in range(n-1, -1, -1):
            # Cantidad de elementos a la derecha que son mayores que positions[i]
            right = query(n - 1) - query(positions[i])
            result += left[i] * right
            update(positions[i], 1)
        
        return result
        