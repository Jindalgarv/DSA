class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr=set(nums)
        arr=list(arr)
        arr= self.bucket_sort(arr)
        n= len(arr)
        k=1
        maxi=1
        for i in range(n-1):
            if arr[i+1]-arr[i]==1:
                k+=1
                maxi=max(maxi,k)
            else:
                k=1
        return maxi
                


    def bucket_sort(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        
        n = len(arr)
        min_val, max_val = min(arr), max(arr)
        
        if min_val == max_val:
            return arr[:]
        
        buckets = [[] for _ in range(n)]
        
    
        for num in arr:
            index = int((num - min_val) / (max_val - min_val) * (n - 1))
            buckets[index].append(num)
        
        for bucket in buckets:
            bucket.sort()
        
        result = []
        for bucket in buckets:
            result.extend(bucket)
        
        return result
        