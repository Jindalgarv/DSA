class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree,outdegree=[0]*n,[0]*n
        for a,b in trust:
            indegree[b-1]+=1
            outdegree[a-1]+=1
        for i, deg in enumerate(outdegree):
            if deg==0 and indegree[i]==n-1:
                return i+1
        return -1

            