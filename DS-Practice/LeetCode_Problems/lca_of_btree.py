# Lowset Common Ancestor of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return root
        
        if root == p or root == q:
            return root
        
        left_val = self.lowestCommonAncestor(root.left, p, q)
        right_val = self.lowestCommonAncestor(root.right, p, q)
        
        if left_val and right_val:
            return root
        
        if not left_val and not right_val:
            return None
        
        return left_val if left_val else right_val
        
        
            
