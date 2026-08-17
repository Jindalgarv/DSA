
class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[1]*(n)
        for i in range(2,int(n**.5)+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=0

        return sum(prime[2:])