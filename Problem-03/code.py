class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = len(nums)
        nums_copy = nums[:]  
        for num in nums_copy:
            if num == val:
                nums.remove(num)
                x = x - 1
        print(nums)
        return x

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
instance = Solution()
k = instance.removeElement(nums, 2)
print(k)
