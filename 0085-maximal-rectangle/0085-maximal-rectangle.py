class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        if not matrix or not matrix[0]:
            return 0

        maxArea = 0
        heights = [0]*(n+1)

        for r in matrix:
            for c in range(n):
                if r[c]=='1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            stack = [-1]
            for i in range(len(heights)):
                while heights[stack[-1]]>heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    maxArea = max(maxArea,h*w)
                stack.append(i)

        return maxArea