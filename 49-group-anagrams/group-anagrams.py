class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            arr=[0]*26
            for ch in s:
                arr[ord(ch)-ord('a')]+=1
            t=tuple(arr)
            d[t].append(s)
        output=[]
        for key,values in d.items():
            output.append(values)
        return output
        
        