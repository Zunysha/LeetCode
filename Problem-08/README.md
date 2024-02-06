# **Problem:**
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

# **Examples:**
## Example 1:

Input: nums = [2,2,1]
Output: 1

## Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

## Example 3:

Input: nums = [1]
Output: 1

# **Solution:**
## Intuition

1. **Convert List to Set:**
   - `set(nums)`: Converts the list `nums` into a set, removing any duplicate elements. In the resulting set, each unique number from the original list appears only once.

2. **Calculate Sum of Unique Numbers:**
   - `sum(set(nums))`: Calculates the sum of unique numbers in the set. This sum effectively doubles the sum of each unique number in the original list since each unique number appears twice in the set.

3. **Double the Sum of Unique Numbers:**
   - `2 * sum(set(nums))`: Doubles the sum of unique numbers, accounting for the fact that in the original list, every number except the single one appears twice.

4. **Calculate Sum of All Numbers in the Original List:**
   - `sum(nums)`: Calculates the sum of all numbers in the original list. Since the single number appears only once, and all other numbers appear twice, this sum includes the single number only once.

5. **Find the Single Number:**
   - `2 * sum(set(nums)) - sum(nums)`: Subtracts the sum of all numbers in the original list from the doubled sum of unique numbers. The result is the single number that appears only once in the list.



## Approach
Certainly! The provided code is a Python class named `Solution` with a method `singleNumber`. The purpose of the method is to find and return the single number that appears only once in an array of integers. Here's a step-by-step explanation of the code:

1. **Class Definition:**
   ```python
   class Solution(object):
   ```
   This line defines a class named `Solution`.

2. **Method Definition:**
   ```python
   def singleNumber(self, nums):
   ```
   This line defines a method named `singleNumber` within the `Solution` class. It takes two parameters: `self` (representing the instance of the class) and `nums` (which is expected to be a list of integers).

3. **Method Implementation:**
   ```python
   return 2 * sum(set(nums)) - sum(nums)
   ```
   The method uses a mathematical approach to find the single number:
   - `set(nums)`: Converts the list `nums` into a set, removing any duplicates.
   - `sum(set(nums))`: Calculates the sum of unique numbers.
   - `2 * sum(set(nums))`: Doubles the sum of unique numbers.
   - `sum(nums)`: Calculates the sum of all numbers in the original list.
   - `2 * sum(set(nums)) - sum(nums)`: Subtracts the sum of all numbers from the doubled sum of unique numbers. The result is the single number that appears only once.

4. **Class Instance and Test Data:**
   ```python
   instance = Solution()
   nums = [2, 2, 1]
   ```
   An instance of the `Solution` class is created, and a test list of integers is defined.

5. **Method Invocation:**
   ```python
   instance.singleNumber(nums)
   ```
   The `singleNumber` method is called on the instance with the test list `nums`. The result is not printed or stored in this example, but you can use `print(instance.singleNumber(nums))` to see the output.

In the given example, the output would be `1`, as it is the number that appears only once in the list `[2, 2, 1]`.

## Complexity

### Time Complexity:
The time complexity of the code is determined by the set operations and the summation of the elements in the list.

- Creating a set from the list (`set(nums)`): Constructing a set involves iterating through each element in the list once. Therefore, the set creation has a time complexity of O(n), where n is the number of elements in the list.
  
- Calculating the sum of the set elements (`sum(set(nums))`): Summing the elements of the set also has a time complexity of O(n), where n is the number of unique elements in the set.
  
- Calculating the sum of all elements in the original list (`sum(nums)`): Summing the elements in the original list also has a time complexity of O(n), where n is the number of elements in the list.

The dominant factor for time complexity is the set creation and summation, so the overall time complexity is O(n).

### Space Complexity:
The space complexity of the code is determined by the additional space used for the set.

- Creating a set from the list (`set(nums)`): The space required for the set is O(n), where n is the number of elements in the list. This is because in the worst case, all elements of the list could be unique.

Hence, the overall space complexity is O(n) due to the set created from the list.
