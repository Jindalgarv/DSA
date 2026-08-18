class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #SOLUTION 1 WITH O(1) SPACE
        # for _ in range(k):
        #     num=nums.pop()
        #     nums.insert(0,num)

#SOLUTION 2
        # arr=[]
        # for _ in range(k):
        #     arr.append(nums.pop())
            
        # nums=arr+nums
#OPTIMAL SOLUTION
        n=len(nums)
        k=k%n
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]