class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cmap = {}
        l = 0
        maxl = 0

        for r, ch in enumerate(s):
            if ch in cmap and cmap[ch]>=l:
                l = cmap[ch]+1

            cmap[ch] = r

            maxl = max(maxl,r - l + 1)
        return maxl

            
