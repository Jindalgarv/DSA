class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#O(N2) SOLUTION 
        # res=[]
        # for x in nums1:
        #     for i in range(len(nums2)):
        #         if nums2[i]==x:
        #             a=0
        #             for j in range(i,len(nums2)):
        #                 if nums2[j]>x:
        #                     res.append(nums2[j])
        #                     a=1
        #                     break
        #             if a==0:
        #                 res.append(-1)
        # return res

# O(N) using monotonic stack
        stack = []
        nge = {}
        n1,n2=len(nums1),len(nums2)
        for i in range(n2 - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                nge[nums2[i]] = stack[-1]
            else:
                nge[nums2[i]] = -1

            stack.append(nums2[i])

        return [nge[x] for x in nums1]
