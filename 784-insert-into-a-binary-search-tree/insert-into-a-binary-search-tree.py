# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr=root
        while root:
            if root.val<val and root.right:
                root=root.right
            elif root.val<val:
                root.right=TreeNode(val)
                break
            elif root.left:
                root=root.left
            else:
                root.left=TreeNode(val)
                break
        return curr
        