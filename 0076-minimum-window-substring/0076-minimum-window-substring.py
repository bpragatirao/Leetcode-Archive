class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dt = Counter(t)
        req = len(dt)
        l, r = 0, 0
        res = 0
        count = {}
        ans = float("inf"), None, None
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            if s[r] in dt and count[s[r]] == dt[s[r]]:
                res += 1
            while l <= r and res == req:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                count[s[l]] -= 1
                if s[l] in dt and count[s[l]] < dt[s[l]]:
                    res -= 1
                l += 1    
            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]