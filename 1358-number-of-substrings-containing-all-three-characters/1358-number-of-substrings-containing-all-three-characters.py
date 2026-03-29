class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cmap = {"a": -1,"b": -1,"c": -1}
        c = 0

        for i, ch in enumerate(s):
            cmap[ch] = i
            mini = min(cmap.values())
            if mini != -1:
                c += (mini+1)

        return c