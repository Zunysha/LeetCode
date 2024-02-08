# **Problem:**
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# **Examples:**
## Example 1:

- Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
- Output: [1,2,2,3,5,6]
- Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

## Example 2:

- Input: nums1 = [1], m = 1, nums2 = [], n = 0
- Output: [1]
- Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

## Example 3:

- Input: nums1 = [0], m = 0, nums2 = [1], n = 1
- Output: [1]
- Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# **Constraints:**

- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -109 <= nums1[i], nums2[j] <= 109

# **Solution:**

## Intuition

1. **Replace Elements from `nums2` into `nums1`**: Replace the trailing zeros in `nums1` starting from index `m` with the elements from `nums2`.

2. **Sort `nums1`**: Sort the entire `nums1` array to maintain the sorted order.

3. **Print Modified `nums1`**: Display the modified `nums1` array after the merging and sorting operations.


##  Approach

The approach of the given code is to merge two sorted arrays `nums1` and `nums2` in-place, with `nums1` having additional space at the end to accommodate the elements from `nums2`. The merging process involves the following steps:

1. **Replace Elements**: `nums1[m:] = nums2`: This line replaces the elements in `nums1` starting from index `m` with the elements from `nums2`. It assumes that `nums1` has enough extra space (represented by zeros) to accommodate the elements from `nums2`.

2. **Sort Array**: `nums1.sort()`: After merging the elements from `nums2` into `nums1`, the entire `nums1` array is sorted in ascending order using the `sort()` method. Sorting is necessary because the previous operation may disrupt the sorted order.

3. **Print Result**: `print(nums1)`: This line prints the modified `nums1` after the merging and sorting operations.

### Step-by-Step Breakdown

1. **Replace Elements from `nums2` into `nums1`**: Replace the trailing zeros in `nums1` starting from index `m` with the elements from `nums2`.

2. **Sort `nums1`**: Sort the entire `nums1` array to maintain the sorted order.

3. **Print Modified `nums1`**: Display the modified `nums1` array after the merging and sorting operations.

This approach ensures that the merged array, `nums1`, is sorted while utilizing the additional space provided at the end of `nums1`.

## Complexity

### Time Complexity:
1. Copying elements from `nums2` to `nums1` with `nums1[m:] = nums2` takes O(n) time, where 'n' is the size of `nums2`.
2. Sorting the merged array with `nums1.sort()` takes O((m + n) * log(m + n)) time, where 'm' is the size of `nums1` and 'n' is the size of `nums2`.

Therefore, the overall time complexity is O((m + n) * log(m + n)).

### Space Complexity:
The space complexity of the code is O(1) because it uses a constant amount of extra space regardless of the input size. The modifications are done in-place, and no additional data structures are created.
