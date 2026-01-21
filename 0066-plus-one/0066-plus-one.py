class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        for i in digits:
            l.append(str(i))
        s = "".join(l)
        s = int(s)+1
        s = str(s)
        l=[]
        for i in s:
            l.append(int(i))
        return l
       