# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []

        def build(start,end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                for left in build(start, i-1):
                    for right in build(i+1,end):
                        root = TreeNode(i,left,right)
                        res.append(root)
            return res
        return build(1,n)
