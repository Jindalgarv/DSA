class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        dp=[1]*n
        words.sort(key=len)
        def some_function(s1,s2):
            m,n=len(s1),len(s2)
            if m!=n+1:
                return False
            first,second=0,0
            while first<m and second<n:
                if s1[first]==s2[second]:
                    first,second=first+1,second+1
                else:
                    first+=1
            return second==n

        for i in range(n):
            for j in range(i):
                if some_function(words[i],words[j]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
