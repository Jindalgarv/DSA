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

