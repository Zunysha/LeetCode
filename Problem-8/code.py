class Solution(object):
    def singleNumber(self, nums):  
     return 2*sum(set(nums))-sum(nums)
instance=Solution()
nums=[2,2,1]
instance.singleNumber(nums)  