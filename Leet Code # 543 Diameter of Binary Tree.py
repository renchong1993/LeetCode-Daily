# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def depth(root):
            if not root: 
                return -1
            
            right = depth(root.right)
            left = depth(root.left)
            
            self.res = max(self.res, 2 + left + right)
            
            return max(left, right) + 1
        
        depth(root)
        return self.res
