class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for num in nums:
            if num not in d.keys():
                d[num]=0
            d[num]+=1
            if d[num] >1:
                return True
        return False 

        