class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # n=len(people)
        # m=0
        # for start,end in flowers:
        #     m=max(m,end)
        # diff=[0]*(m+1)
        # for start,end in flowers:
        #         diff[start-1]+=1
        #         diff[end]-=1
        # for i in range(1,m+1):
        #     diff[i]+=diff[i-1]
        # ans=[]
        # for x in people:
        #     if x<m+1:
        #         ans.append(diff[x-1])
        #     else:
        #         ans.append(0)
        # return ans

        starts=sorted([start for start, end in flowers])
        ends=sorted([end for start,end in flowers])
        ans=[]
        for t in people:
            ans.append(bisect_right(starts,t)-bisect_left(ends,t))
        return ans