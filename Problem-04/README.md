# Problem Statement:

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not found, return the index where it would be if inserted in order. The algorithm must have a runtime complexity of O(log n).

# **Examples:**

## Example 1:

Input: nums = [1, 3, 5, 6], target = 5
Output: 2

## Example 2:

Input: nums = [1, 3, 5, 6], target = 2
Output: 1


## Example 3:
Input: nums = [1, 3, 5, 6], target = 7
Output: 4

## Constraints:

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4

# **Solution:**
## Intutuion

### Check if the Target is Present:

The method starts by checking if the target is already present in the given list `nums` using the `in` operator. If the target is found, it retrieves the index of the target in the existing list using `nums.index(target)`. This index is assigned to the variable `x`.

### If Target is Not Present:

If the target is not present in the list, it is appended to the end of the list using `nums.append(target)`. After appending, the list is sorted in ascending order using `nums.sort()`.

### Find the Index of the Target:

After sorting, the index of the target in the modified list is found using `nums.index(target)`. This index is again assigned to the variable `x`.

### Print Sorted List and Return Result:

The sorted list is printed to show the updated state of `nums`. The method returns the index `x`, which represents the position where the target should be inserted to maintain the sorted order.

## Approach:

The provided code defines a class `Solution` containing a method `searchInsert` designed to find the insertion index of a target value within a sorted list of integers (`nums`). The algorithm utilizes binary search to efficiently locate the insertion point while maintaining two pointers, `low` and `high`, representing the current search space. The method iteratively calculates the middle index (`mid`) and compares the element at that index (`nums[mid]`) with the target value. Depending on the comparison, the search space is adjusted by updating the pointers. If the target is found, the method returns the index; otherwise, it returns the `low` pointer, representing the position where the target should be inserted to maintain the sorted order. The code also prints the modified list `nums`.

### Initialize Pointers:

Set two pointers, `low` and `high`, to define the current search space. `low` starts at the beginning (index 0), and `high` starts at the end (index `len(nums) - 1`).

### Binary Search Loop:

Use a while loop to perform binary search until the `low` pointer is greater than the `high` pointer. Calculate the middle index (`mid`) of the current search space.

### Check Middle Element:

Compare the middle element (`nums[mid]`) with the target value. If they are equal, return the index `mid` as the target is found. If `nums[mid]` is less than the target, update `low` to `mid + 1` to search the right half. If `nums[mid]` is greater than the target, update `high` to `mid - 1` to search the left half.

### Print List and Return Insertion Point:

If the target is not found during the binary search, print the original list `nums`. Return the `low` pointer, which represents the position where the target should be inserted to maintain the sorted order.

### Example Usage:

Define a sorted list `nums` and a target value `target`. Create an instance of the `Solution` class. Call the `searchInsert` method with `nums` and `target`. Print the result, which is the index where the target should be inserted.

This approach utilizes the binary search algorithm to efficiently find the insertion point of the target in a sorted list. The time complexity is O(log n), where n is the length of the input list `nums`.

## Complexity:

### Time Complexity:

The time complexity of the binary search algorithm implemented in this code is O(log n), where n is the length of the input list `nums`. In each iteration of the while loop, the search space is divided in half, resulting in a logarithmic time complexity.

### Space Complexity:

The space complexity of this code is O(1) since it uses a constant amount of extra space that does not depend on the input size. The algorithm modifies the pointers `low` and `high` iteratively but does not use any additional data structures that scale with the input size. Therefore, it has constant space complexity.
