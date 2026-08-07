class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax,remain=0,income
        x=0
        if remain>brackets[0][0]:
            remain=remain-brackets[0][0]
            tax+=brackets[0][0]*brackets[0][1]/100
        else:
            return remain*brackets[0][1]/100
        i=0
        while remain>0:
            diff=brackets[i+1][0]-brackets[i][0]
            if remain>diff:
                remain-=diff
                tax+=diff*brackets[i+1][1]/100
                i+=1
            else:
                break
        tax+=remain*brackets[i+1][1]/100
        return tax


        