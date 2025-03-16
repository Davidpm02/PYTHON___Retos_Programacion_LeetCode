"""
DESCRIPTION:

You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

 

Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

Example 2:

Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

 

Constraints:

    1 <= ranks.length <= 105
    1 <= ranks[i] <= 100
    1 <= cars <= 106

"""

from typing import List
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        """
        Se encarga de hallar el tiempo mínimo posible que lleva
        a los mecánicos reparar 'n' coches.

        El número de coches a reparar viene dado por el valor 
        que tome el parámetro 'cars'.

        params:
            ranks (List[int])
            cars (int)
        
        returns:
            int
        """

        def canRepairInTime(time):
            # Calculamos cuántos coches se pueden reparar en 'time'
            total_cars = 0
            for r in ranks:
                # Un mecánico con rank r puede reparar x coches si r * x^2 <= time
                max_cars = int((time // r) ** 0.5)  # Resolviendo x^2 <= time / r
                total_cars += max_cars
                if total_cars >= cars:
                    return True  # Ya encontramos un tiempo suficiente
            return False  # No podemos reparar todos los coches en este tiempo

        # Búsqueda binaria en el tiempo mínimo necesario
        low, high = 1, min(ranks) * (cars ** 2)  # Peor caso, un solo mecánico los repara
        while low < high:
            mid = (low + high) // 2
            if canRepairInTime(mid):
                high = mid  # Intentamos reducir el tiempo
            else:
                low = mid + 1  # Necesitamos más tiempo
        return low