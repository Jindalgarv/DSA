class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        arr=[]
        res=[]
        for key, value in freq.items():
            arr.append((value,key))
            arr.sort(reverse=True)
        for n,ch in arr:
            res.append(ch*n)
        return "".join(res)
            