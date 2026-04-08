class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec=[]
        out=0
        for x in operations:
            if x=='+':
                rec.append(rec[-1]+rec[-2])
            elif x=='D':
                rec.append(rec[-1]*2)
            elif x=='C':
                rec.pop()
            else:
                rec.append(int(x))
        for x in rec:
            out+=x
        return out