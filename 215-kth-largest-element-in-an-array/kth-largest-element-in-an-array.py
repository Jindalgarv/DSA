class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for x in nums:
            heappush(heap,x)
            if len(heap)>k:
                heappop(heap)
        return heap[0]
        