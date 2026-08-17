class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n=len(word)
        ans=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                if word[j] not in 'aeiou':
                    break
                seen.add(word[j])
                if(len(seen))==5:
                    ans+=1
        return ans