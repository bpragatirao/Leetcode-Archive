class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dt = Counter(t)
        req = len(dt)
        l, r = 0, 0
        f = 0
        count = {}
        ans = float("inf"), None, None
        while r < len(s):
            ch = s[r]
            count[ch] = count.get(ch, 0) + 1
            if ch in dt and count[ch] == dt[ch]:
                f += 1
            while l <= r and f == req:
                ch = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                count[ch] -= 1
                if ch in dt and count[ch] < dt[ch]:
                    f -= 1
                l += 1    
            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]