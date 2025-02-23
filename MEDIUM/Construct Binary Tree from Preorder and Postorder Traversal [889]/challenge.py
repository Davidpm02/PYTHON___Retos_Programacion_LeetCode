"""
DESCRIPTION:

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]

 

Constraints:

    1 <= preorder.length <= 30
    1 <= preorder[i] <= preorder.length
    All the values of preorder are unique.
    postorder.length == preorder.length
    1 <= postorder[i] <= postorder.length
    All the values of postorder are unique.
    It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        """
        Se encarga de construir un árbol binario a partir de dos listas
        de sus elementos, preordenados y postordenados,

        params:
            preorder (List[int])
            postorder (List[int])
        
        returns:
            Optional[TreeNode]
        """
        
        # Caso base: si no hay nodos en preorder, retornamos None
        if not preorder:
            return None
        
        # Creamos la raíz con el primer elemento de preorder
        root = TreeNode(preorder[0])
        
        # Si solo hay un nodo, retornamos directamente
        if len(preorder) == 1:
            return root
        
        # Encontramos el índice del primer nodo del subárbol izquierdo en postorder
        left_subtree_root_idx = postorder.index(preorder[1])
        
        # Construimos recursivamente los subárboles izquierdo y derecho
        root.left = self.constructFromPrePost(preorder[1:left_subtree_root_idx + 2], postorder[:left_subtree_root_idx + 1])
        root.right = self.constructFromPrePost(preorder[left_subtree_root_idx + 2:], postorder[left_subtree_root_idx + 1:-1])
        
        return root