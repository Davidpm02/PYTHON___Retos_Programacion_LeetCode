"""
DESCRIPTION:

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

  2 ==> 4 ==> 3
  5 ==> 6 ==> 4
  
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]



Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 
"""


## IMPORTS -----------

from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
          Summary:
              Función parametrizada que se encarga de llevar a cabo un proceso de conversión de dos arrays de
              entrada, a un array de salida, que contenga, como elementos, los dígitos que componen el resultado
              de la suma de los enteros representados por los arrays de entrada.
              
          Args:
              l1 -- Primer array de entrada.
              l2 -- Segundo array de entrada.
              
          Returns:
              nodes_array -- Array generado, cuyos elementos son los dígitos que componen el resultado de la operación
                            que se lleva a cabo dentro de la función.
        """
        
        # Convierto las entradas en listas de Python
        l1 = self.iterar_lista_enlazada(l1)
        l2 = self.iterar_lista_enlazada(l2)
        
        
        ## Saneo las entradas, evaluando las restricciones
        
        # 1era restricción
        assert len(l1) > 0 and len(l1) <= 100    # Primer array
        assert len(l2) > 0 and len(l2) <= 100    # Segundo array
        
        # 2da restricción
        try:
          self.checkNodes(l1)
          self.checkNodes(l2)
        except AssertionError:
          return "Los parámetros de entrada no cumplen las restricciones del enunciado."
        
        ## LÓGICA ----------------
        
        # Invierto el orden de los arrays de entrada
        l1 = l1[::-1]
        l2 = l2[::-1]
        
        # Casteo a strings los números de los arrays
        l1 = [str(_) for _ in l1]
        l2 = [str(_) for _ in l2]
        
        
        # Convierto los arrays a entero
        integer_1 = int("".join(l1))
        integer_2 = int("".join(l2))
        
        # Opero los enteros procesados
        sum_result = integer_1 + integer_2
        
        # Convierto el resultado en una lista
        nodes_array = [int(_) for _ in str(sum_result)][::-1]
        
        # Convierto la lista en objeto ListNode
        list_node_object = self.turnArrayToListNode(nodes_array)
        
        # Retorno la lista invertida
        return list_node_object
        
        
        
    def checkNodes(self, node_list):
      
      """Función auxiliar parametrizada que se encarga de comprobar que los nodos de los array recibidos como parámetros
         no cumplen la restricción mencionada en el enunciado del problema."""
         
      for n in node_list:
        assert n >= 0 and n <= 9   # Rango [0, 9]
        
    def iterar_lista_enlazada(self, nodo):
      
      """Función auxiliar que se encarga de iterar sobre los nodos del objeto ListNode recibido como parámetro."""
      
      array = []
      while nodo is not None:
          array.append(nodo.val)
          # Avanzo al siguiente nodo en la lista
          nodo = nodo.next
          
      # Retorno el array generado
      return array
    
    def turnArrayToListNode(self, array):
      
      """Función auxiliar encargada de procesar el array generado por la clase Solution, y convertilo en objeto
         ListNode."""
      
      # Defino un objeto ListNode con atributos por defecto
      head = ListNode()
      
      # Asigno una variable de referencia que apunte al objeto ListNode inicializado
      actual = head
      
      # Itero sobre cada elemento de la lista generada por la clase Solution
      for num in array:
        
        # Defino como valor para el atributo next del objeto ListNode, un nuevo objeto
        # ListNode
        actual.next = ListNode(num)

        # Reasigno la variable de referencia al siguiente nodo del objeto ListNode
        actual = actual.next
    
      return head.next   # Retorno la continuación del primer objeto ListNode
      
      
      
        
      
        
        
if __name__ == "__main__":
  
  l1 = ListNode([1, 2, 3])
  l2 = ListNode([5, 6, 4])
  sol = Solution()
  resultado = sol.addTwoNumbers(l1, l2)
  print(resultado)
  
  
