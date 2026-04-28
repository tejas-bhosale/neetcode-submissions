# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSorthelper(pairs, 0, len(pairs) - 1)

    def mergeSorthelper(self,pairs: List[Pair],start:int,end:int)-> List[Pair]:
        if (end-start)+1 <= 1:
            return pairs
        
        mid = (start+end)//2

        self.mergeSorthelper(pairs,start,mid)
        self.mergeSorthelper(pairs,mid+1,end)

        self.merge(pairs,start,mid,end)
        return pairs
        
    def merge(self,arr:List[Pair],start:int,mid:int,end:int) -> None:

        L = arr[start:mid+1]
        R = arr[mid+1:end+1]

        i=0
        j=0
        k=start

        while i<len(L) and j<len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i <len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


