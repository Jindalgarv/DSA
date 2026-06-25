# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        dfs(root)
        l,r=0,len(inorder)-1
        while l<r:
            if inorder[l]+inorder[r]>k:
                r-=1
            elif inorder[l]+inorder[r]<k:
                l+=1
            else:
                return True
        return False