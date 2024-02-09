# **Problem:**
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

# **Examples:**
## Example 1:

- Input: nums = [0,1,0,3,12]
- Output: [1,3,12,0,0]
  
## Example 2:

- Input: nums = [0]
- Output: [0]
 

# **Constraints:**

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

# **Solution:**

## Approach

1. **Class Definition:**
   - The code defines a class `Solution` with a method `moveZeroes`.
   - `moveZeroes` takes a list of integers (`nums`) as input and modifies it in-place.

2. **Iteration over `nums`:**
   - The code uses a for loop to iterate through each element (`num`) in the list `nums`.

3. **Condition Check:**
   - Inside the loop, there is an `if` statement checking if the current element (`num`) is equal to 0.

4. **Moving Zeroes:**
   - If the current element is 0, it removes that element from its current position in the list using `nums.remove(num)`.
   - Then, it appends the removed zero to the end of the list using `nums.append(num)`.

5. **Printing Result:**
   - After the loop, the modified list `nums` is printed using `print(nums)`.


## Complexity

### Time Complexity:

The time complexity of this code is O(n^2), where 'n' is the length of the input list `nums`.

- The `for num in nums:` loop iterates through each element in the list, and for each iteration, there is a call to `nums.remove(num)`.
- The `remove` operation has a time complexity of O(n) because, in the worst case, it may need to shift all elements after the removed element to fill the gap.

Since this removal operation is nested within the loop, the overall time complexity becomes O(n^2).

### Space Complexity:

The space complexity of this code is O(1) because it uses a constant amount of additional space regardless of the input size.

- The only space used is for the loop variable `num`, and the modification is done in-place without using any extra data structures proportional to the input size.

