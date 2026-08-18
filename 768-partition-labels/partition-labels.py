class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ={}
        output=[]
        for i in range(len(s)-1,-1,-1):
            if s[i] not in last_occ:
                last_occ[s[i]]=i
        prev,last=0,0
        for i in range(len(s)):
            last=max(last,last_occ[s[i]])
            if last==i:
                output.append(i-prev+1)
                prev=last+1
        return output

        