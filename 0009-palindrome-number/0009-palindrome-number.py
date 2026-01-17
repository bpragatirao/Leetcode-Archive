class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = []
        prev=""
        for i in str(x):
            if i=="-":
                prev="-"
                continue
            elif prev=="-":
                i=prev+i
                prev=""
                num.append(int(i))
            else:
                num.append(int(i))
        flag = 0
        l,r = 0,len(num)-1

        while l<=r:
            if num[l]==num[r]:
                l+=1
            elif num[l]!=num[r]:
                flag = 1
            elif x==-1:
                flag = 1
            r-=1

        return False if flag==1 or x==-1 else True