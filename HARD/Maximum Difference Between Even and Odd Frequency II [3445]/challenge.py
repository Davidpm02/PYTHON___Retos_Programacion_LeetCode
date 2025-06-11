"""
DESCRIPTION:

You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:

subs has a size of at least k.
Character a has an odd frequency in subs.
Character b has an even frequency in subs.
Return the maximum difference.

Note that subs can contain more than 2 distinct characters.

 

Example 1:

Input: s = "12233", k = 4

Output: -1

Explanation:

For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

Example 2:

Input: s = "1122211", k = 3

Output: 1

Explanation:

For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

Example 3:

Input: s = "110", k = 3

Output: -1

 

Constraints:

3 <= s.length <= 3 * 10^4
s consists only of digits '0' to '4'.
The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
1 <= k <= s.length

"""

import math

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        
        """
        Encuentra la diferencia máxima freq[a] - freq[b] en cualquier
        substring de tamaño >= k, donde freq[a] es impar y freq[b] es
        par.

        params:
            s (str)
            k (int)
        
        returns:
            int
        """

        n = len(s)
        # 1) Construyo prefijos de conteo para cada dígito '0'..'4'
        counts = {c: [0] * (n + 1) for c in '01234'}
        for i, ch in enumerate(s, start=1):
            for c in counts:
                # Yo actualizo para cada dígito, heredando y sumando si coincide
                counts[c][i] = counts[c][i-1] + (1 if ch == c else 0)

        ans = float('-inf')

        # Mapeo de paridad (pa,pb) a un índice 0..3
        def parity_idx(p):
            return p[0] * 2 + p[1]

        for a in '01234':
            for b in '01234':
                if a == b:
                    continue

                # 2) arr[i] = conteo de a hasta i  -  conteo de b hasta i
                arr = [counts[a][i] - counts[b][i] for i in range(n + 1)]
                # paridad de cada prefijo para (a, b)
                parity = [(counts[a][i] & 1, counts[b][i] & 1) for i in range(n + 1)]
                # recuento de b en cada prefijo
                bcount = counts[b]

                # Configuro tamaño del segment tree según el máximo bcount
                max_b = bcount[-1]
                # next power of two ≥ max_b+1
                size = 1 << (math.ceil(math.log2(max_b + 1)) if max_b > 0 else 0)
                if size == 0:
                    size = 1

                # 4) Cuatro árboles, uno por cada grupo de paridad (pa,pb)
                trees = [[float('inf')] * (2 * size) for _ in range(4)]

                # Funciones auxiliares para actualizar y consultar
                def st_update(tree, pos, val):
                    """Yo actualizo la posición pos con min(current, val)."""
                    p = pos + size
                    if val < tree[p]:
                        tree[p] = val
                        p //= 2
                        while p:
                            tree[p] = min(tree[2*p], tree[2*p + 1])
                            p //= 2

                def st_query(tree, l, r):
                    """Yo consulto el mínimo en el rango [l, r] inclusive."""
                    res = float('inf')
                    l += size
                    r += size
                    while l <= r:
                        if l & 1:
                            res = min(res, tree[l])
                            l += 1
                        if not (r & 1):
                            res = min(res, tree[r])
                            r -= 1
                        l //= 2
                        r //= 2
                    return res

                # Recorro i como extremo derecho
                for i in range(k, n + 1):
                    # 4.1) inserto l = i-k en el árbol correspondiente a su paridad
                    l = i - k
                    idx_l = parity_idx(parity[l])
                    st_update(trees[idx_l], bcount[l], arr[l])

                    # 4.2) decido qué grupo de paridad de l necesito:
                    #     para que freq[a] sea impar: pa_l = 1 - pa_r
                    #     para que freq[b] sea par:  pb_l = pb_r
                    pa_r, pb_r = parity[i]
                    needed = (1 - pa_r, pb_r)
                    idx_need = parity_idx(needed)

                    # 4.3) exijo que bcount[l] < bcount[i] (es decir freq[b] > 0)
                    bi = bcount[i]
                    if bi - 1 >= 0:
                        best = st_query(trees[idx_need], 0, bi - 1)
                        if best != float('inf'):
                            # la diferencia arr[i] - arr[l] = freq[a] - freq[b]
                            ans = max(ans, arr[i] - best)

        return ans if ans != float('-inf') else -1