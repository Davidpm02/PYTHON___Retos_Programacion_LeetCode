"""
DESCRIPTION:

You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:

Input: s = "NSWWEW", k = 3

Output: 6

Explanation:

Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

 

Constraints:

1 <= s.length <= 10^5
0 <= k <= s.length
s consists of only 'N', 'S', 'E', and 'W'.

"""

import heapq

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # I start by mapping each move to its delta (dx, dy).
        moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        n = len(s)
        max_dist = 0
        # I consider the four Manhattan objectives by projecting onto (dx, dy).
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for obj_dx, obj_dy in directions:
            # I build the list of contributions and benefits per move.
            contribs = []      # original projection v_i
            benefits = []      # benefit of changing to best move (1 instead of v_i)
            for move in s:
                dx, dy = moves[move]
                v = obj_dx * dx + obj_dy * dy
                contribs.append(v)
                # best replacement always contributes +1 in this projection.
                benefits.append(1 - v)

            # I use two heaps to maintain the top-k benefits dynamically.
            selected = []      # min-heap of chosen benefits (size <= k)
            available = []     # max-heap (as negative) of remaining benefits
            sum_sel = 0        # sum of chosen benefits
            prefix_sum = 0     # cumulative sum of original contribs

            for i in range(n):
                prefix_sum += contribs[i]
                b = benefits[i]
                if b > 0:
                    # push into available
                    heapq.heappush(available, -b)
                # if I can take more, move best beneficial
                if len(selected) < k and available:
                    best = -heapq.heappop(available)
                    heapq.heappush(selected, best)
                    sum_sel += best
                # or swap if a better benefit is available
                elif available and selected and -available[0] > selected[0]:
                    # I replace the smallest in selected with the largest in available
                    old = heapq.heappop(selected)
                    new = -heapq.heappop(available)
                    sum_sel += new - old
                    heapq.heappush(selected, new)
                # compute best for this prefix
                curr = prefix_sum + sum_sel
                max_dist = max(max_dist, curr)

        return max_dist
