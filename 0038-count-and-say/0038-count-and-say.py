class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        
        for i in range(n - 1):
            next_res = ""
            count = 1
            for j in range(len(res)):
                if j + 1 < len(res) and res[j] == res[j+1]:
                    count += 1
                else:
                    next_res += str(count) + res[j]
                    count = 1    
            res = next_res
            
        return res