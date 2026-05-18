class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            # print(f'prefix = {prefix}')
            left[i] = nums[i]*prefix
            # print(f'left[i] = {left[i]}')
            prefix = prefix * nums[i]
            # print(f'prefix = {prefix}')
            # print("")

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            # print(nums[i])
            right[i] = nums[i] * postfix
            postfix *= nums[i]
            # print(f'left {left}')
            # print(f'right {right}')
        ans = [0]*len(nums)
        for i in range(len(nums)):
            left_portion = left[i-1] if i-1 >=0 else 1
            right_portion = right[i+1] if i+1 < (len(nums)) else 1
            ans[i] = left_portion*right_portion
        return ans
                


            