class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch = {}
        l, maxi = 0, 0
        res = 0
        n = len(s)

        for r in range(n):
            ch[s[r]] = 1 + ch.get(s[r],0)
            maxi = max(maxi,ch[s[r]])

            while (r-l+1) - maxi > k:
                ch[s[l]]-=1
                l+=1

            res = max(res,(r-l+1))

        return res
            