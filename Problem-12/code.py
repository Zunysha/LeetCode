class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        actual_sum=n*(n+1)//2
        list_sum=sum(nums)
        return actual_sum-list_sum
nums=[3,0,1]
s=Solution()
s.missingNumber(nums)