class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        i,n=0,len(intervals)
        while i<n:
            j=i+1
            newinterval=intervals[i]
            while j<n and newinterval[1]>=intervals[j][0]:
                newinterval[0]=min(newinterval[0],intervals[i][0])
                newinterval[1]=max(newinterval[1],intervals[j][1])
                j+=1
            res.append(newinterval)
            i=j
        return res


