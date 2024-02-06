class Solution(object):
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        print(nums)
        return low

nums = [1, 3, 5, 6]
target = 2
instance = Solution()
print(instance.searchInsert(nums, target))
