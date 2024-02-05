# **Problem:**
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# **Examples:**
## Example 1:

Input: nums = [3,2,3]
Output: 3
## Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

# **Constraints:**

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109

# **Solution:**
## Intuition
The code is an implementation of the **Boyer-Moore Voting Algorithm**, a clever algorithm for finding the majority element in an array efficiently with a constant amount of space. The majority element in an array is an element that appears more than n/2 times, where n is the length of the array.

#### Intuition behind the algorithm:

1. The algorithm maintains two variables: `candidate` and `count`. The `candidate` represents the potential majority element, and `count` keeps track of its frequency.

2. It iterates through the array, and for each element:
   - If `count` is 0, it updates the `candidate` to the current element.
   - If the current element is the same as the candidate, it increments the count.
   - If the current element is different from the candidate, it decrements the count.

3. The algorithm essentially "cancels out" pairs of different elements. If there is a majority element, it will survive this process, as it occurs more than n/2 times.

4. At the end of the iteration, the `candidate` variable holds the potential majority element. To confirm if it's the actual majority element, you might need a second pass through the array to count its occurrences.

The key insight is that if there is a majority element, it will survive the cancellation process and end up as the final candidate. The algorithm is efficient with O(n) time complexity and O(1) space complexity, making it suitable for large arrays.


## Approach
The provided code implements the **Boyer-Moore Voting Algorithm** to find the majority element in a given list (`nums`). Here's the approach of the code:

1. **Initialization:** The algorithm initializes two variables, `candidate` and `count`. These variables will be used to track the potential majority element and its count.

2. **Iterative Process:** The algorithm iterates through the elements of the input list (`nums`).
   - If the `count` is 0, it means that there is no current candidate, so the algorithm sets the `candidate` to the current element.
   - For each element, it checks if the element is equal to the current `candidate`. If it is, the `count` is incremented; otherwise, the `count` is decremented.
   - This process essentially "cancels out" pairs of different elements, and the candidate survives as the potential majority element.

3. **Result:** At the end of the iteration, the `candidate` variable holds the potential majority element.

4. **Time Complexity:** The algorithm makes a single pass through the input list, so the time complexity is O(n), where n is the length of the input list.

5. **Space Complexity:** The algorithm uses only a constant amount of space, as it maintains only two variables (`candidate` and `count`). Therefore, the space complexity is O(1).

6. **Return:** The algorithm returns the potential majority element as the result.

7. **Test Code:** The provided test code creates an instance of the `Solution` class and tests the `majorityElement` method with two example lists (`[3,2,3]` and `[2,2,1,1,1,2,2]`), printing the results.

The key insight of the Boyer-Moore Voting Algorithm is to efficiently find the majority element in linear time and constant space by canceling out pairs of different elements.


## Complexity
### Time complexity:
The time complexity of this algorithm is O(n), where n is the length of the input list `nums`. This is because the algorithm iterates through the list once, performing constant time operations in each iteration.
### Space complexity
The space complexity is O(1) because the algorithm uses a constant amount of space regardless of the size of the input list. The only variables used are `candidate` and `count`, and their space requirements do not depend on the size of the input list.
