class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sub = start ^ goal

        count = 0
        while sub >= 1:
            sub = sub & (sub-1)
            count += 1
        
        return count
