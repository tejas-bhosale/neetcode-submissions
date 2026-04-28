class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            differ = target - nums[i]
            if nums[i] in d.keys():
                return [d[nums[i]],i]
            d[differ] = i
            
        
        