# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root.val
        if not root:
            return
        if curr<p.val and curr<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif curr>p.val and curr>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
        
        