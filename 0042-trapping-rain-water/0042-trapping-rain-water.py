class Solution:
    def trap(self, height: List[int]) -> int:
        maxl, maxr, total = 0, 0, 0
        n = len(height)
        l, r = 0, n-1

        while (l<r):
            if height[l] <= height[r]:
                if maxl > height[l]:
                    total += maxl - height[l]
                else:
                    maxl = height[l]
                l += 1

            else:
                if maxr > height[r]:
                    total += maxr - height[r]
                else:
                    maxr = height[r]
                r -= 1

        return total 