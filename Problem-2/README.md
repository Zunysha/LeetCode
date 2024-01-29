# **Problem:**

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
2. The remaining elements of `nums` are not important, as well as the size of `nums`.
3. Return `k`.

# **Examples:**

*Example 1:*

Input: `nums = [1, 1, 2]`  
Output: `2`, `nums = [1, 2, _]`  
Explanation: Your function should return `k = 2`, with the first two elements of `nums` being 1 and 2 respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

*Example 2:*

Input: `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`  
Output: `5`, `nums = [0, 1, 2, 3, 4, _, _, _, _, _]`  
Explanation: Your function should return `k = 5`, with the first five elements of `nums` being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

# **Constraints:**

- 1 <= `nums.length` <= 3 * 10^4
- -100 <= `nums[i]` <= 100
- `nums` is sorted in non-decreasing order.


# **Solution:**
## Intuition
The code defines a class `Solution` with a method `removeDuplicates` designed to operate on a list of integers (`nums`). The objective is to identify and count the unique elements in the list while maintaining the original order.

1. `new_list`: This list is used to store unique elements as they are encountered during the iteration through `nums`.

2. `unique_count`: This variable keeps track of the count of unique elements.

3. Iteration: The code iterates through each element (`p`) in the input list (`nums`).

4. Conditional Check: For each element, it checks whether it is already present in `new_list`. If not, it appends the element to `new_list` and increments the `unique_count`. If the element is already in `new_list`, it is skipped.

5. Result: The code prints the `new_list`, which now contains the unique elements, and returns the `unique_count`.

6. Example Usage: The class is instantiated, and the `removeDuplicates` method is called with the sample input `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`. The result is the count of unique elements and the list of unique elements: `[0, 1, 2, 3, 4]`.

In summary, the intuition behind this code is to identify and count unique elements in a list, maintaining the original order, and providing the results as the count of unique elements and the list containing those unique elements.


## Approach
The code defines a class `Solution` with a method `removeDuplicates` that operates on a list of integers (`nums`). The objective is to remove duplicates in-place and return the number of unique elements. The approach involves modifying the array `nums` such that the first `k` elements contain the unique elements in the original order.

1. **Initialization:**
    - `unique`: Initialized to 1, as the first element is considered unique.
    - `index`: Initialized to 1, as it keeps track of the position where the next unique element should be placed.

2. **Iteration through the List:**
    - The code iterates through the list `nums` starting from the second element (`i = 1`) to the end.

3. **Checking for Duplicates:**
    - For each element, it checks whether it is equal to the previous element (`nums[i] != nums[i - 1]`). If true, it means a new unique element is found.

4. **Updating the Array:**
    - If a new unique element is found, it is placed at the correct position (`nums[index] = nums[i]`).
    - `index` is then incremented to prepare for the next unique element.
    - `unique` is also incremented to keep track of the count of unique elements.

5. **Return:**
    - The method returns the variable `unique`, representing the count of unique elements.

6. **Example Usage:**
    - An instance of the `Solution` class is created, and the `removeDuplicates` method is called with the sample input `my_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`.
    - The result (`k`) is the count of unique elements.
    - The modified array (`my_list[:k]`) containing the first `k` unique elements is printed.
    - The count of unique elements (`k`) is also printed.

**Summary:**
The approach focuses on iterating through the array, identifying unique elements, and modifying the array in-place to contain only the unique elements in the original order. The final result is the count of unique elements and the modified array with the first `k` unique elements. This approach avoids using additional space and efficiently updates the array while maintaining its non-decreasing order.

## Complexity
**- Time Complexity:**

The time complexity of the provided code is O(n), where n is the length of the input list nums. The primary reason for this linear time complexity is the single loop that iterates through each element of the list once.

In the loop, the code performs constant time operations such as comparisons (nums[i] != nums[i - 1]), assignments (nums[index] = nums[i]), and increments (index += 1 and unique += 1). As the number of operations inside the loop is constant, the overall time complexity is proportional to the number of elements in the input list, resulting in a linear time complexity of O(n).

  **- Space Complexity:**

The space complexity is O(1) because the code uses a constant amount of additional space regardless of the size of the input list. The main variables contributing to space complexity are unique and index, both of which require a constant amount of space.

The code modifies the input list in-place without using any additional data structures that depend on the size of the input. Therefore, the space complexity remains constant, and it is denoted as O(1).


