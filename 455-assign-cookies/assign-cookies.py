class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(),s.sort()
        n,m=len(g),len(s)
        l,r=0,0
        while l<m and r<n:
            if g[r]<=s[l]:
                r=r+1
            l+=1
        return r
            








        # if not g or not s:
        #     return 0
        # g.sort()
        # s.sort()
        # biggest=s[-1]
        # count=0
        # for num in g:
        #     k=0
        #     while True:
        #         if num+k in s:
        #             s.remove(num+k)
        #             count+=1
        #             break
        #         elif num+k>biggest:
        #             return count
        #         k+=1
        # return count

        