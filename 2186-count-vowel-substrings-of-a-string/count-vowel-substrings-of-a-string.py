class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n=len(word)
        ans=0
        for i in range(n):
            if word[i] not in 'aeiou':
                continue
            for j in range(i,n):
                if word[j] not in 'aeiou':
                    break
                if len(set(word[i:j+1]))==5:
                    ans+=1
        return ans