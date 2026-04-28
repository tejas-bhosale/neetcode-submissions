from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec = deque()
        res = []
        l=r=0

        while r<len(nums):
            while dec and nums[dec[-1]] < nums[r]:
                dec.pop()
            dec.append(r)

            if l > dec[0]:
                dec.popleft()
            if (r+1) >=k:
                res.append(nums[dec[0]])
                l+=1
            r+=1
        return res

        