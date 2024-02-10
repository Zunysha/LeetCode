class NumArray:
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self,left,right):
        return sum(self.nums[left:right+1])
nums=[1,2,3,4,5]
obj=NumArray(nums)
print(obj.sumRange(1,3))