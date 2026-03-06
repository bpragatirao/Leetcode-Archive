class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        pmap = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
    
        res = []
    
        def combo(i, s):
            if i == len(digits):
                res.append(s)
                return

            l = pmap[digits[i]]
        
            for char in l:
                combo(i + 1, s + char)
            
        combo(0, "")
        return res