from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        sorted_map=sorted(freq.items(),key= lambda x:x[1],reverse=True)
        res=[]
        for key, value in sorted_map:
            res.append(key)
        return res[0:k]
        
        