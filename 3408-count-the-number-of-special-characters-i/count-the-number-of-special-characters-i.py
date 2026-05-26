class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower,upper=set(),set()
        for x in word:
            if x.islower():
                lower.add(x)
            else:
                upper.add(x.lower())
        return(len(lower & upper))
        