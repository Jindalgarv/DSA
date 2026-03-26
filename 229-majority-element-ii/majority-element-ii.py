class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        out=[]
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for (key,value) in d.items():
            if value>len(nums)/3:
                out.append(key)
        return out
        