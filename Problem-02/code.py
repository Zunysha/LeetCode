class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        unique = 1  
        index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
                unique += 1

        return unique
my_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
instance = Solution()
k = instance.removeDuplicates(my_list)
print( my_list[:k])
print(k)
