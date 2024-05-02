"""
DESCRIPTION:

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

## TODO ==> Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

  Input: lists = [[1,4,5],[1,3,4],[2,6]]
  Output: [1,1,2,3,4,4,5,6]
  Explanation: The linked-lists are:
  [
    1->4->5,
    1->3->4,
    2->6
  ]
  merging them into one sorted list:
  1->1->2->3->4->4->5->6


Example 2:

  Input: lists = []
  Output: []


Example 3:

  Input: lists = [[]] 
  Output: []
 

## Constraints:

  k == lists.length
  0 <= k <= 104
  0 <= lists[i].length <= 500
  -104 <= lists[i][j] <= 104
  lists[i] is sorted in ascending order.
  The sum of lists[i].length will not exceed 104.
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Método de la clase Solution encargado de generar un objeto de la clase ListNode
           formado por todos los elementos contenidos en cada ListNode del parámetro 'lists',
           pero ordenados ascendentemente.
           
           Args:
               - lists -- Array de objetos ListNode cuyo contenido será procesado por la función.
               
           Returns:
               - ListNode -- Objeto ListNode con el resultado.
        """
        
        def process_listNode(listNode_object, values_in_listNode_object):
          
          """
          """
          if listNode_object == None:
            return listNode_object
          
          value_val = listNode_object.val
          values_in_listNode_object.append(value_val)
          
          listNode_object = listNode_object.next
          # Llamo recursivamente a la función de procesamiento del ListNode
          process_listNode(listNode_object, values_in_listNode_object)
          
        def create_listNode(values, prev_node=None):

            """
            """

            # Verifico si la lista 'values' está vacía y devuelvo el nodo inicial si es así
            if not values:
                return prev_node
            
            # Creo el primer nodo si 'prev_node' es None (caso de la primera llamada)
            if prev_node is None:
                prev_node = ListNode(values[0])
                head = prev_node  # Guardo el nodo cabeza de la lista para retornarlo al final
            else:
                # Creo un nuevo nodo y lo enlazo con el anterior
                prev_node.next = ListNode(values[0])
                prev_node = prev_node.next
            
            # Llamo recursivamente a la función con el resto de la lista
            # Utilizo slicing para evitar modificar la lista original
            create_listNode(values[1:], prev_node)

            # Devuelvo el nodo cabeza de la lista sólo desde la primera llamada
            return prev_node if prev_node else None
          
        
        
        
        
        
        # Defino una lista inicialmente vacía
        values_array = []
        
        # Inicialmente, se deberá procesar el array de objetos ListNodes,
        # e ingresar todos los elementos dentro de la lista 'values_array'.
        for listNode_object in lists:
          values_in_listNode_object = []
          process_listNode(listNode_object, values_in_listNode_object)
          
          # Una vez procesado, añado el contenido a la lista inicial
          values_array.append(values_in_listNode_object)
          continue
        
        # Cuando se procese todo el contenido del parámetro,
        # proceso el contenido de la lista
       
        ordered_values_array = [value for list_ in values_array for value in list_]
        ordered_values_array = sorted(ordered_values_array)
        print(ordered_values_array)
        
        # Creo el objeto ListNode a retornar por el método
        listNode_object = create_listNode(values = ordered_values_array)
        print(listNode_object)
        return listNode_object
      
      
      
      
if __name__ == "__main__":
  
  lists = [[1,4,5],[1,3,4],[2,6]]
  solution = Solution()
  sol = solution.mergeKLists(lists= lists)
  print(sol)