class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
    
        res, i, sign = 0, 0, 1
        MAX, MIN = 2**31 - 1, -2**31
    
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
        
            if res > (MAX - digit) // 10:
                return MAX if sign == 1 else MIN
        
            res = res * 10 + digit
            i += 1
        
        return max(MIN, min(res * sign, MAX))

        