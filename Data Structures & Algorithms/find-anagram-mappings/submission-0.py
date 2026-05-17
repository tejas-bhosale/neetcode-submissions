class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d= {}
        for i in range(len(nums2)):
            if nums2[i] not in d.keys():
                d[nums2[i]] = []
            d[nums2[i]].append(i)
        ans=[]
        for i in range(len(nums1)):
            ans.append(d[nums1[i]][0])
            d[nums1[i]].pop(0)
        return ans

        