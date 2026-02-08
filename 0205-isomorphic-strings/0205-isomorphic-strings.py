class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1,map2={},{}

        for cs,ct in zip(s,t):

            if cs in map1:
                if map1[cs]!=ct:
                    return False
            
            if ct in map2:
                if map2[ct]!=cs:
                    return False

            map1[cs]=ct
            map2[ct]=cs
            
        return True