"""
DESCRIPTION:

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:

Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:

Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:

Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

 

Constraints:

    The number of nodes in the original tree is in the range [1, 1000].
    1 <= Node.val <= 109

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        """
        Se encarga de recuperar un arbol binario a partir de una cadena
        de texto cada, que representa la estructura en cuanto a valores
        de los nodos y los diferentes niveles que este tiene.

        params:
            traversal (str)
        
        returns:
            Optional[TreeNode]
        """
        
        stack = []  # Pila para rastrear los nodos
        i = 0  # Índice para recorrer la cadena
        
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1  # Contamos los guiones para la profundidad
            
            start = i  # Inicio del número
            while i < len(traversal) and traversal[i].isdigit():
                i += 1  # Extraemos el número completo
            
            value = int(traversal[start:i])  # Convertimos el valor a entero
            node = TreeNode(value)
            
            # Si la pila tiene más elementos de la profundidad actual, retrocedemos en un elemento
            while len(stack) > depth:
                stack.pop()
            
            # Conectamos el nuevo nodo con su padre
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Añadimos el nodo actual a la pila
            stack.append(node)
        
        return stack[0]  # La raíz del árbol es el primer nodo agregado
