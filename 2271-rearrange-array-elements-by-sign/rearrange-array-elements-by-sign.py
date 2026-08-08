class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=deque()
        neg=deque()
        while nums:
            x=nums.pop()
            if x>0:
                pos.appendleft(x)
            else:
                neg.appendleft(x)
        for x,y in zip(pos,neg):
            nums.append(x)
            nums.append(y)
        return nums
            