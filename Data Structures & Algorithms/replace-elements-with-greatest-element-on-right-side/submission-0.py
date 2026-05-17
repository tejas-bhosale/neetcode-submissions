class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = arr[-1]
        arr[-1] = -1
        r = len(arr)-2
        while r>=0:
            temp = arr[r]
            arr[r] = max_val
            max_val = max(temp,max_val)
            r-=1
        return arr
        