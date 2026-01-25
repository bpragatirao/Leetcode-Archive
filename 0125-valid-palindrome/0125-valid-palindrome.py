class Solution:
    def isPalindrome(self, s: str) -> bool:
        t =""
        for i in range(len(s)):
            if s[i].isalnum():
                t+=s[i].lower()

        f = 0
        l,r = 0,len(t)-1
        while l<=r:
            if t[l]==t[r]:
                l+=1
            else:
                f = 1
            r-=1

        return f==0
