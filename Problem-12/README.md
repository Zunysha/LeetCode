# **Problem:**
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# **Examples:**
## Example 1:

- Input: nums = [3,0,1]
- Output: 2
- Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
## Example 2:

- Input: nums = [0,1]
- Output: 2
- Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
  
## Example 3:

- Input: nums = [9,6,4,2,3,5,7,0,1]
- Output: 8
- Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# **Constraints:**

- n == nums.length
- 1 <= n <= 104
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

# **Solution:**

## Intuition
1. **Initialize a variable `count` to 0:** This variable represents the expected next number in the sequence.

2. **Iterate over the range from 0 to `len(nums) + 1`:** This range covers all possible numbers in the sequence, including the one that might be missing.

3. **Inside the loop, check if the current value of `count` is present in the given array `nums`:** If `count` is found in `nums`, increment `count` to check the next number.

4. **If `count` is not found in `nums`, return it as the missing number.**

5. **If the loop completes without finding a missing number, return -1:** This indicates that no missing number was found.



## Approach

1. **Determine the length of the list (`n`):** Get the length of the input list `nums` and store it in the variable `n`.

2. **Calculate the expected sum (`actual_sum`):** Use the formula for the sum of consecutive numbers from 0 to n, which is `n * (n + 1) // 2`. Store this value in the variable `actual_sum`. This represents the sum of all numbers in the range from 0 to n.

3. **Calculate the sum of the given list (`list_sum`):** Use the `sum` function to find the sum of all elements in the list `nums`. Store this value in the variable `list_sum`.

4. **Find the missing number:** Subtract the `list_sum` from the `actual_sum`. The result represents the missing number in the list.

5. **Return the missing number:** The missing number is then returned by the method.

In summary, the approach relies on the mathematical concept of the sum of consecutive numbers to find the missing element efficiently. By calculating the expected sum and subtracting the actual sum of the given list, the code identifies and returns the missing number.

## Complexity
Let's analyze the time and space complexity of the provided code:

### Time Complexity:
- Calculating the length of the list (`n`) takes O(1) time as it is a constant-time operation.
- The operations involved in calculating `actual_sum` and `list_sum` both take constant time, O(1).
- The overall time complexity is dominated by the summation operations, and calculating the difference `actual_sum - list_sum` also takes constant time.
- Therefore, the time complexity of the code is O(1).

### Space Complexity:
- The space complexity is also constant, O(1), as the code uses a fixed amount of additional space for variables (`n`, `actual_sum`, `list_sum`).
- There are no data structures or recursive calls that would lead to space consumption proportional to the size of the input.
