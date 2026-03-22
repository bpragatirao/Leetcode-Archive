class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxa = 0
        n = len(heights)

        for i in range(n):
            while (stack and heights[stack[-1]] > heights[i]):
                ele = stack[-1]
                stack.pop()
                nse = i
                if stack:
                    pse = stack[-1]
                else:
                    pse = -1
                maxa = max(maxa,heights[ele]*(nse-pse-1))
            stack.append(i)

        while stack:
            nse = n
            ele = stack[-1]
            stack.pop()
            if stack:
                pse = stack[-1]
            else:
                pse = -1
            maxa = max(maxa,heights[ele]*(nse-pse-1))

        return maxa