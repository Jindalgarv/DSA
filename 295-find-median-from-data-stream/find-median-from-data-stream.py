class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        if len(self.minheap)==len(self.maxheap)==0:
            heappush(self.minheap,num)
        elif len(self.minheap)==len(self.maxheap):
            if num<(-self.maxheap[0]):
                heappush(self.minheap,-heappop(self.maxheap))
                heappush(self.maxheap,-num)
            else: heappush(self.minheap,num)
        else:
            if num>=self.minheap[0]:
                heappush(self.maxheap,-heappop(self.minheap))
                heappush(self.minheap,num)
            else:
                heappush(self.maxheap,-num)

    def findMedian(self) -> float:
        if not self.minheap and not self.maxheap:
            return []
        elif len(self.minheap)==len(self.maxheap):
            return (self.minheap[0]-self.maxheap[0])/2
        else:
            return self.minheap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()