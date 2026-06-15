from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #SOLUTION 1 NOT THE MOST OPTIMAL
        # freq=Counter(nums)
        # sorted_map=sorted(freq.items(),key= lambda x:x[1],reverse=True)
        # res=[]
        # return [key for key,value in sorted_map[0:k]]

        #SOLUTION 2 USING HEAP
        # freq=Counter(nums)
        # heap=[]
        # for key, value in freq.items():
        #     heappush(heap,(value,key))
        #     if len(heap)>k:
        #         heappop(heap)
        # res=[]
        # for value,key in heap:
        #     res.append(key)
        # return res

#SOLUTION 3 USING BUCKET SORT
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


        
        