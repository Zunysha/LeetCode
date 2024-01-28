
 # **Problem:**

Given an array of integers `nums` and an integer `target`, return the indices of two numbers in the array such that their sum equals the target. You can assume that each input has exactly one solution, and the same element cannot be used twice. The order of the returned indices does not matter.

# **Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

# **Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

# **Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

# **Constraints:**

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
  
# **Solution:**
## Intuition
Nested loops involve placing one loop inside another, creating a multi-level loop structure. Each iteration of the outer loop triggers the inner loop to run through its iterations. This is commonly used for iterating through two-dimensional arrays or performing repetitive tasks with multiple layers of conditions. While nested loops provide flexibility, they can lead to increased time complexity and should be used judiciously. Alternative approaches like using functions or optimizing algorithms may be considered for efficiency.

## Approach
This code defines a class Solution with a method twoSum that finds indices of two numbers in the input list nums whose sum equals the given target. It uses a set (sets) to efficiently check for complement values, and a single pass through the input list using enumerate. If a complement is found in the set, it returns the indices; otherwise, it adds the current number to the set. The code has a time complexity of O(n) and space complexity of O(n).

## Complexity
- Time complexity:
The code iterates through the input list once, using a set to efficiently check for complement values. Set operations, such as lookup and addition, have constant time complexity, resulting in an overall time complexity of O(n), where n is the length of the input list.

- Space complexity:
The space complexity is O(n) because the code uses a set to store unique numbers from the input list. If the input list has n unique elements, the set will have to store all of them, resulting in space usage proportional to the size of the input list, which is O(n).



