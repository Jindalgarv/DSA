class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for x in d:
            if d[x]>1:
                return True
        return False
        
        