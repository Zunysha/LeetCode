# **Problem:**
Given an integer array nums, handle multiple queries of the following type:

- Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

    - NumArray(int[] nums) Initializes the object with the integer array nums.
    - int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
 # **Examples:**
 ## Example 1:

- Input
  
["NumArray", "sumRange", "sumRange", "sumRange"]

[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
- Output : 
[null, 1, -1, -3]

- Explanation
    - NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    - numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    - numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    - numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
    - 
# **Solution:**

 ## Approach
1. **Initialization:**
   - The class `NumArray` has an `__init__` method that takes an array `nums` as input and initializes the attribute `self.nums` with this input array.

2. **Sum Range Method:**
   - The class has a method named `sumRange` that calculates the sum of elements in a specified range `[left, right]` (inclusive).
   - It uses Python's slicing notation (`self.nums[left:right + 1]`) to extract the subarray from index `left` to `right`.
   - The `sum()` function is then applied to calculate the sum of elements in this subarray.
   - The result is returned.

3. **Example Usage:**
   - An instance of the `NumArray` class is created with the array `[1, 2, 3, 4, 5]`.
   - The `sumRange` method is called with arguments `1` and `3` to calculate the sum of elements between indices 1 and 3 (inclusive).
   - The result is printed.

**Summary:**
   - The code encapsulates the functionality of calculating the sum of elements in a specified range within a class.
   - It uses the `sum()` function and slicing notation to efficiently calculate the sum of the specified subarray.
   - The class allows for easy instantiation with different arrays, and the `sumRange` method provides a convenient way to query the sum within different ranges.
  

## Complexity

### Time Complexity:
- The `__init__` method has a time complexity of O(N), where N is the length of the input array `nums`. This is because it simply initializes the attribute `self.nums` with the input array.

- The `sumRange` method, when called, extracts a subarray using slicing notation (`self.nums[left:right + 1]`) and then calculates the sum using the built-in `sum()` function. The time complexity of this operation is O(K), where K is the size of the subarray (`right - left + 1`).

- In the worst case, if you call `sumRange` repeatedly with different ranges, the overall time complexity could be O(Q * K), where Q is the number of queries and K is the average size of the subarray.

### Space Complexity:
- The space complexity of the `__init__` method is O(N) because it stores the entire input array `nums` in the attribute `self.nums`.

- The `sumRange` method does not use any additional space that scales with the input size; it only performs calculations on the existing array. Therefore, its space complexity is O(1).