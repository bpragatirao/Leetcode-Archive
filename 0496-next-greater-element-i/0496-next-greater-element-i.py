class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        def nextgr(n,s):
            for i in s:
                if i>n:
                   return i
            return -1
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    res.append(nextgr(nums1[i],nums2[j+1:]))
        
        return res if len(res)==len(nums1) else []