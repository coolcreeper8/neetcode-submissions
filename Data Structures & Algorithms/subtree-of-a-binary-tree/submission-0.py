# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def equals(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False
            
            leftequals = equals(root.left, subRoot.left)
            rightequals = equals(root.right, subRoot.right)

            if leftequals and rightequals:
                return root.val == subRoot.val

            return False
        
        if root is None:
            return subRoot is None
        
        if equals(root, subRoot):
            return True
        else:
            return Solution.isSubtree(self, root.left, subRoot) or Solution.isSubtree(self, root.right, subRoot)

