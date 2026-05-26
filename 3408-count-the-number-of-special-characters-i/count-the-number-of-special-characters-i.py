class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=0
        for x in set(word):
            if chr(ord(x)+32) in set(word):
                s+=1
        return s
        