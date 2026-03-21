class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            while stack and curr < 0 and stack[-1] > 0:
                diff = curr + stack[-1]
                
                if diff < 0:
                    stack.pop()
                    continue
                elif diff > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                if not (stack and curr < 0 and stack[-1] > 0):
                    stack.append(curr)
                    
        return stack