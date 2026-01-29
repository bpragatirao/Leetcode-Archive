class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        
        longest = ""
        for i in range(len(s)):
            p1 = self.expand(s, i, i)
            p2 = self.expand(s, i, i + 1)
            longest = max(longest, p1, p2, key=len)
        return longest

    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1 : r]