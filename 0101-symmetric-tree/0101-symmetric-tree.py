# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        return self.isSame(root.left,root.right)

    def isSame(self,a,b):

        if not a and not b:
            return True

        if not a or not b or a.val != b.val:
            return False

        return self.isSame(a.left,b.right) and self.isSame(a.right,b.left)