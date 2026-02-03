class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n1,n2,l = [],[],[]
        for i in nums:
            n2.append(i) if i<0 else n1.append(i)
        for i in range(len(n1)):
            l.append(n1[i])
            l.append(n2[i])
        return l