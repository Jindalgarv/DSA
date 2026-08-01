class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        if not len(self.maxheap):
            heappush(self.maxheap,-num)
        elif num<=-self.maxheap[0]:
            heappush(self.maxheap,-num)
        else:
            heappush(self.minheap,num)

        if len(self.maxheap)<len(self.minheap):
            heappush(self.maxheap,-heappop(self.minheap))
        if len(self.maxheap)>len(self.minheap)+1:
            heappush(self.minheap,-heappop(self.maxheap))
       

    def findMedian(self) -> float:
        if len(self.maxheap)==len(self.minheap):
            return (self.minheap[0]-self.maxheap[0])/2
        return -self.maxheap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()