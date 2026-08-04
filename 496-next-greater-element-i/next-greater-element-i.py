class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for x in nums1:
            for i in range(len(nums2)):
                if nums2[i]==x:
                    a=0
                    for j in range(i,len(nums2)):
                        if nums2[j]>x:
                            res.append(nums2[j])
                            a=1
                            break
                    if a==0:
                        res.append(-1)
        return res
                