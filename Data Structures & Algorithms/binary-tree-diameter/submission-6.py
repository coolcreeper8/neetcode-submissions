# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        paths = []
        def abb(root):
            if root is None: 
                return 0

            leftpath = abb(root.left)
            rightpath = abb(root.right)

            paths.append(leftpath + rightpath)
            return 1 + max(leftpath, rightpath)
        
        abb(root)
        return max(paths) if paths else 0   