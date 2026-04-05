# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = []
        queue = [(root, 0, 0)]
        
        while queue:
            node, col, row = queue.pop(0)

            if node:
                nodes.append((col,row,node.val))
                queue.append((node.left, col-1, row+1))
                queue.append((node.right, col+1, row+1))
        
        nodes.sort()
        res = []

        if not nodes:
            return res

        prev_col = nodes[0][0]
        curr_col = []

        for col, row, val in nodes:
            if prev_col == col:
                curr_col.append(val)
            else:
                res.append(curr_col)
                curr_col = [val]
                prev_col = col

        res.append(curr_col)
        return res