class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def total(op):
            n = len(nums)
            left = [0] * n
            right = [0] * n
            
            stack = []
            for i in range(n):
                while stack and (nums[stack[-1]] > nums[i] if op == "min" else nums[stack[-1]] < nums[i]):
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack = []
            for i in range(n - 1, -1, -1):
                while stack and (nums[stack[-1]] >= nums[i] if op == "min" else nums[stack[-1]] <= nums[i]):
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)
            
            return sum(nums[i] * left[i] * right[i] for i in range(n))

        return total("max") - total("min")