from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count=Counter(nums)
        for num,freq in count.items():
            heappush(heap,(freq,num))
            if len(heap)>k:
                heappop(heap)
        ans=[]
        for freq,num in heap:
            ans.append(num)
        return ans

#SOLUTION 3 USING BUCKET SORT MOST OPTIMAL
        freq = Counter(nums)
        bucket=[[] for _ in range(len(nums)+1)]
        for key,value in freq.items():
            bucket[value].append(key)
        res=[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res

