# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        
        def helper(root, left):
            if not root:
                return 0

            if not root.left and not root.right and left == True:
                self.sum += root.val
                      
            helper(root.left, True)
            helper(root.right, False)
    
        
        helper(root, False)
        return self.sum
