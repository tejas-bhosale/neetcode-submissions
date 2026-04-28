# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quicksort_method(pairs,0,len(pairs)-1)

    def quicksort_method(self,arr: List[Pair],start:int,end:int)-> List[Pair]:
        if end-start+1<=1:
            return arr
        pivot = arr[end]
        left = start

        for i in range(start,end):
            if arr[i].key<pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left+=1
        arr[end] = arr[left]
        arr[left] = pivot
        self.quicksort_method(arr,start,left-1)
        self.quicksort_method(arr,left+1,end)
        return arr

    