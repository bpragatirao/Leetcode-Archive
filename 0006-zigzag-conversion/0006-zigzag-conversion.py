class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = []
        res = []
        sl = list(s)
        row=0
        flag = 0
        if numRows==1 or numRows>len(s):
            return s
        for i in range(numRows):
            l.append([])
        for i in s:
            l[row].append(i)
            if row==0 or row==numRows-1:
                flag = not flag
            row +=1 if flag else -1
        
        for i in l:
            res+=i
        return "".join(res)
            