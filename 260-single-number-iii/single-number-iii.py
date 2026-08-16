class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num=0
        for x in nums:
            num=num^x
        i=0
        while True:
            k=1<<i
            if num&k:
                idx=k
                break
            i+=1
        num1,num2=0,0
        for x in nums:
            if x&idx==0:
                num1=num1^x
            else:
                num2=num2^x
        return [num1,num2]



        
        