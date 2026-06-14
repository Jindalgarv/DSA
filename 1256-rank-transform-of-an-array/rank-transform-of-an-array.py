class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        positions={}
        for i,num in enumerate(sorted_arr,start=1):
            positions[num]=i
        for i,num in enumerate(arr):
            arr[i]=positions[arr[i]]
        return arr