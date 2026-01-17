class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        res = 0
        if x < 0:
            res = int(s[1:][::-1])
            result = res * -1
        else:
            result = int(s[::-1])
        if result < (-2)**31 or result > (2**31)-1 :
            return 0
        else:
            return result
