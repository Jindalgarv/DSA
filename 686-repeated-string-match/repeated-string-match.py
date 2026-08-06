class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n1,n2=len(a),len(b)
        n=n2//n1+4
        c=""
        for i in range(n):
            c+=a
            if b in c:
                return i+1
        return -1