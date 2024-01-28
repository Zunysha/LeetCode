class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sets = set()
        for i, num in enumerate(nums):
            comp = target - num
            if comp in sets:
                return [nums.index(comp), i]
            sets.add(num)
        return None

instance = Solution()
print(instance.twoSum([2, 7, 11, 15], 9))

