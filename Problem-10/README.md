# **Problem:**
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# **Examples:**
## Example 1:

Input: rowIndex = 3

Output: [1,3,3,1]

## Example 2:

Input: rowIndex = 0

Output: [1]

## Example 3:

Input: rowIndex = 1

Output: [1,1]
 

# **Constraints:**

- 0 <= rowIndex <= 33

# **Solution:**

## Approach:
1. **Initialize an empty list `tri`:**
   - This list (`tri`) will represent Pascal's Triangle, where each element is a row containing coefficients.

    ```python
    tri = []
    ```

2. **Iterate through rows up to `rowIndex`:**
   - The outer loop runs for `rowIndex + 1` iterations, creating rows up to the specified `rowIndex`.

    ```python
    for i in range(rowIndex + 1):
    ```

3. **Create a new row with all elements initialized to 1:**
   - Each row is represented as a list (`row`), and the elements are initially set to 1.

    ```python
    row = [1] * (i + 1)
    ```

4. **Update the elements in the middle of the row:**
   - The inner loop starts from 1 and goes up to `i - 1` (exclusive). It updates the elements in the middle of the row based on the values from the previous row.

    ```python
    for j in range(1, i):
        row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
    ```

5. **Append the current row to the triangle:**
   - Once the current row is complete, it is appended to the `tri` list, representing Pascal's Triangle.

    ```python
    tri.append(row)
    ```

6. **Return the requested row:**
   - Finally, the method returns the specified row from the generated Pascal's Triangle.

    ```python
    return tri[rowIndex]
    ```

7. **Instantiate the Solution class and test with `rowIndex = 3`:**
   - The last few lines of code create an instance of the `Solution` class (`s`) and call the `getRow` method with `rowIndex = 3`. The result is then printed.

    ```python
    s = Solution()
    result = s.getRow(3)
    print(result)
    ```

This approach helps in building Pascal's Triangle and retrieving the desired row, and the last part demonstrates how to test it with an example (`rowIndex = 3`).

## Complexity

### Time Complexity:

The time complexity of the code is O(rowIndex^2). This is because, for each row up to the specified `rowIndex`, the code uses nested loops. The outer loop runs rowIndex times, and for each iteration, the inner loop runs i - 1 times (where i is the current row index). As a result, the total number of iterations can be approximated to (1 + 2 + 3 + ... + rowIndex), which is proportional to rowIndex^2.

### Space Complexity:

The space complexity of the code is also O(rowIndex^2). The space required is mainly due to the `tri` list, which stores all the rows of Pascal's Triangle. The maximum number of elements in `tri` is roughly equal to the sum of the first rowIndex natural numbers, leading to the rowIndex^2 growth pattern.


