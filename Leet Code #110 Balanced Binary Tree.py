# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def get_height(root):
            if root is None:
                return 0
            
            l_height, r_height = get_height(root.left), get_height(root.right)
            if l_height < 0 or r_height < 0 or abs(l_height - r_height) > 1:
                return -1
            return max(l_height, r_height) + 1
    
        return (get_height(root) >= 0 )
