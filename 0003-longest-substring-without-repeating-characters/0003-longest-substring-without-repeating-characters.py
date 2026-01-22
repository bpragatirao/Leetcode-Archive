class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cmap = {}
        left = 0
        maxl = 0

        for right, ch in enumerate(s):
            if ch in cmap and cmap[ch]>=left:
                left = cmap[ch]+1

            cmap[ch] = right

            maxl = max(maxl,right - left + 1)
        return maxl

            
