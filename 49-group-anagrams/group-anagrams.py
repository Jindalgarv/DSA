class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        res=[]
        for s in strs:
            ss="".join(sorted(s))
            if ss in d:
                d[ss].append(s)
            else:
                d[ss]=[s]
        for key, value in d.items():
            res.append(value)
        return res
        