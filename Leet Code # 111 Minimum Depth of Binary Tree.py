# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.mindep = float("inf")
        
        if root is None:
            return 0
        
        def height(root, num):
            if not root: return
            
            if not root.left and not root.right:
                self.mindep = min(self.mindep, num)
            
            
            height(root.left, num + 1)
            height(root.right, num + 1)
        
        height(root, 1)
        
        return self.mindep
