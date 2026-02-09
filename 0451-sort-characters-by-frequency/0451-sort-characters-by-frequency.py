from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sorted_chars = sorted(c.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i,f in sorted_chars:
            result.append(i*f)
            
        return "".join(result)
