class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        out=[]
        for x in nums:
                d[x]=d.get(x,0)+1
        for (key,value) in d.items():
            if value>len(nums)/3:
                out.append(key)
        return out
        