# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxi = 0
        def length(x):
            if not x:
                return 0

            leftl = length(x.left)
            rightl = length(x.right)

            total = leftl+rightl
            self.maxi = max(self.maxi,total)

            return int(max(leftl,rightl)+1)

        length(root)
        return self.maxi