"""
DESCRIPTION:

Given a binary tree with the following rules:

    root.val == 0
    For any treeNode:
        If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
        If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2

Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

    FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
    bool find(int target) Returns true if the target value exists in the recovered binary tree.

 

Example 1:

Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 

Example 2:

Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

Example 3:

Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True

 

Constraints:

    TreeNode.val == -1
    The height of the binary tree is less than or equal to 20
    The total number of nodes is between [1, 104]
    Total calls of find() is between [1, 104]
    0 <= target <= 106

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()  # Usamos un conjunto para almacenar los valores recuperados
        self.recover_tree(root, 0)  # Iniciamos la recuperación con la raíz
    
    def recover_tree(self, node: Optional[TreeNode], value: int):
        if node is None:
            return
        
        # Asignamos el valor correcto al nodo y lo almacenamos en el conjunto
        node.val = value
        self.values.add(value)
        
        # Llamadas recursivas para recuperar los nodos izquierdo y derecho
        self.recover_tree(node.left, 2 * value + 1)
        self.recover_tree(node.right, 2 * value + 2)
    
    def find(self, target: int) -> bool:
        return True if (target in self.values) else False