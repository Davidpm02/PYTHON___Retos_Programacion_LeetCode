"""
DESCRIPTION:

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# TODO ==> Return the head of the merged linked list.

 

Example 1:

  Input: list1 = [1,2,4], list2 = [1,3,4]
  Output: [1,1,2,3,4,4]


Example 2:

  Input: list1 = [], list2 = []
  Output: []


Example 3:

  Input: list1 = [], list2 = [0]
  Output: [0]
 

## Constraints:

  The number of nodes in both lists is in the range [0, 50].
  -100 <= Node.val <= 100
  Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        """Método de la clase Solution que se encarga de procesar dos arrays de entrada, y retornar una única lista que
           contenga ordenados todos los elementos dentro de estos dos parámetros.
          
           Args:
               list1 -- Primer array a procesar por el método.
               list2 -- Segundo array a procesar por el método.
               
           Returns:
               listnode -- Objeto de la clase ListNode que contiene, de forma ordenada, todos los elementos de ambos parámetros.
        """
        
        # Comienzo definiendo un objeto ListNode a modo de placeholder, con una cabeza provisional
        node_head = ListNode(-1)
        
        # Instancio una variable que haga de referencia al nodo inicial creado
        prev = node_head
        
        # LÓGICA
        # Itero sobre los parámetros "list1" y "list2", añadiendo contenido al objeto ListNode inicial de manera ordenada.
        while list1 and list2:
          if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
          else:
            prev.next = list2
            list2 = list2.next

          # Reasigno la variable de referencia "prev"
          prev = prev.next
        

        # Me aseguro de incluir el resto del parámetro que aun tenga contenido
        prev.next = list1 if list1 is not None else list2


        if prev is None:

            return ListNode(val = [])

        # Retorno el contenido añadido al objeto ListNode inicial, obviando la cabeza provisional
        return node_head.next      
          
if __name__ == "__main__":
  
  list1 = ListNode(1)
  list1.next = ListNode(3)
  list1.next.next = ListNode(5)
  list2 = ListNode(2)
  list2.next = ListNode(4)
  list2.next.next = ListNode(6)
  solution =  Solution()
  sol = solution.mergeTwoLists(list1= list1,
                               list2= list2)
  print(sol)