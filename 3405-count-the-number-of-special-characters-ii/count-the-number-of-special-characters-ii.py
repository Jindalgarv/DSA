class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        for i in range(0,len(word)):
            if chr(ord(word[i])+32) in word[:i] and chr(ord(word[i])+32) not in word[i+1:] and word[i] not in word[:i]:
                count+=1
        return count
        