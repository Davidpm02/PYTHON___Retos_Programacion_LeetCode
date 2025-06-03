"""
DESCRIPTION:

You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:

status[i] is 1 if the ith box is open and 0 if the ith box is closed,
candies[i] is the number of candies in the ith box,
keys[i] is a list of the labels of the boxes you can open after opening the ith box.
containedBoxes[i] is a list of the boxes you found inside the ith box.
You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.

 

Example 1:

Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Output: 16
Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
Example 2:

Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
Output: 6
Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.
 

Constraints:

n == status.length == candies.length == keys.length == containedBoxes.length
1 <= n <= 1000
status[i] is either 0 or 1.
1 <= candies[i] <= 1000
0 <= keys[i].length <= n
0 <= keys[i][j] < n
All values of keys[i] are unique.
0 <= containedBoxes[i].length <= n
0 <= containedBoxes[i][j] < n
All values of containedBoxes[i] are unique.
Each box is contained in one box at most.
0 <= initialBoxes.length <= n
0 <= initialBoxes[i] < n

"""

from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """
        Dado un conjunto de cajas con estados (abiertas o cerradas),
        cantidad de dulces, llaves y cajas contenidas, junto con una
        lista de cajas iniciales, esta función retorna el número máximo
        de dulces que se pueden recolectar siguiendo las reglas:
          - Solo puedo tomar dulces de cajas abiertas.
          - Al abrir una caja, obtengo las llaves y las cajas que contiene.
          - Si obtengo una llave para una caja que tenía cerrada y conozco
            su existencia, puedo abrirla después.
        
        params:
            status ()
            candies ()
            keys ()
            containedBoxes ()
            initialBoxes ()
        
        returns:
            int
        """
        
        # Conjunto de llaves que tengo disponibles
        llaves = set()
        # Conjunto de cajas que he encontrado (pero podrían estar cerradas)
        cajas_encontradas = set(initialBoxes)
        # Cola para procesar las cajas que estén abiertas y listas para coger sus dulces
        cola = deque()
        # Conjunto para marcar las cajas que ya he procesado (tomado dulces)
        procesadas = set()
        # Cantidad total de dulces recolectados
        total_dulces = 0
        
        # 1. Inicializo: agrego a la cola las cajas que ya están abiertas de las iniciales
        for caja in initialBoxes:
            # Compruebo si la caja inicial está abierta desde el principio
            if status[caja] == 1:
                cola.append(caja)
        
        # 2. Proceso la cola mientras haya cajas abiertas por procesar
        while cola:
            caja_actual = cola.popleft()
            
            # Si ya procesé esta caja, no vuelvo a hacerlo
            if caja_actual in procesadas:
                continue
            
            # Marcar la caja como procesada (ya tomaré sus dulces)
            procesadas.add(caja_actual)
            
            # 2.1. Tomo todos los dulces de la caja
            total_dulces += candies[caja_actual]
            
            # 2.2. Agrego las llaves que obtengo al abrir esta caja
            for llave in keys[caja_actual]:
                # Si obtengo una llave nueva, la agrego
                if llave not in llaves:
                    llaves.add(llave)
                    # Si la caja que abre esta llave ya estaba disponible y no procesada, encolo
                    if llave in cajas_encontradas and llave not in procesadas and status[llave] == 0:
                        # Cambiaré su estado a abierta
                        status[llave] = 1
                        cola.append(llave)
            
            # 2.3. Agrego a mi inventario las cajas contenidas dentro de la caja actual
            for caja_interna in containedBoxes[caja_actual]:
                # Registro que he encontrado esta caja
                if caja_interna not in cajas_encontradas:
                    cajas_encontradas.add(caja_interna)
                    # Si la caja interna ya está abierta o tengo la llave, la encolo
                    if status[caja_interna] == 1 or caja_interna in llaves:
                        status[caja_interna] = 1
                        cola.append(caja_interna)
            
            # 2.4. Reviso si al agregar nuevas llaves podría abrir alguna caja ya encontrada
            # Por cada caja en mi inventario, si la tengo cerrada y ahora tengo la llave, la abro
            # y la agrego a la cola. Esta verificación garantiza que no me quede con cajas abiertas pendientes.
            for caja_existente in list(cajas_encontradas):
                if caja_existente not in procesadas and status[caja_existente] == 0 and caja_existente in llaves:
                    status[caja_existente] = 1
                    cola.append(caja_existente)
        
        return total_dulces