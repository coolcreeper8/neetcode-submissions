# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def find_height(root):
            if root is None:
                return 0
            leftpath = find_height(root.left)
            rightpath = find_height(root.right)


            return max(leftpath, rightpath) + 1
        
        def balanced(root):

            left = 0
            right = 0
            if not root:
                return True
            if root.left:
                left = find_height(root.left)
            if root.right:
                right = find_height(root.right)
            return abs(left - right) <=1 and balanced(root.left) and balanced(root.right)


        return balanced(root)