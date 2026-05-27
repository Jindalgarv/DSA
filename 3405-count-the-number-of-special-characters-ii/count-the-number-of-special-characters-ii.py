class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # count=0
        # for i in range(0,len(word)):
        #     if chr(ord(word[i])+32) in word[:i] and chr(ord(word[i])+32) not in word[i+1:] and word[i] not in word[:i]:
        #         count+=1
        # return count
        idxl=[-1]*26
        idxu=[-1]*26
        for i,x in enumerate(word):
            if x.islower():
                idxl[ord(x)-ord('a')]=i
            elif idxu[ord(x)-ord('A')]==-1:
                idxu[ord(x)-ord('A')]=i
        ans=0
        for i in range(26):
            if idxl[i]>=0 and idxu[i]>=idxl[i]:
                ans+=1
        return ans


        