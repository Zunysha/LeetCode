# **Problem:**
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

# **Examples:**
## Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

## Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

## Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

# **Constraints:**

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's
  
  
# **Solution:**

## Intuition

### Convert to Integer
- Initially, the list of digits `[1, 2, 3]` is converted to a single integer using `int("".join(map(str, digits)))`.
- This step effectively concatenates the digits and converts them to an integer, resulting in `123`.

### Add 1
- One is added to the obtained integer (`result = result + 1`).
- In our example, `123 + 1` equals `124`.

### Convert Back to List of Digits
- The updated integer is then converted back to a list of its digits using `list(map(int, str(result)))`.
- This involves converting `124` to `['1', '2', '4']` as strings.
- Each character is then mapped back to an integer, resulting in `[1, 2, 4]`.

### Return the Result
- The final result, `[1, 2, 4]`, is returned.
- This code essentially treats a list of digits as a number, increments it by 1, and returns the updated list of digits.

## Approach

### Convert to Integer
- Initially, the list of digits `[1, 2, 3]` is converted to a single integer using `int("".join(map(str, digits)))`.
- This step effectively concatenates the digits and converts them to an integer, resulting in `123`.

### Add 1
- One is added to the obtained integer (`result = result + 1`).
- In our example, `123 + 1` equals `124`.

### Convert Back to List of Digits
- The updated integer is then converted back to a list of its digits using `list(map(int, str(result)))`.
- This involves converting `124` to `['1', '2', '4']` as strings.
- Each character is then mapped back to an integer, resulting in `[1, 2, 4]`.

### Return the Result
- The final result, `[1, 2, 4]`, is returned.
- This code essentially treats a list of digits as a number, increments it by 1, and returns the updated list of digits.

## Complexity

### Time Complexity:
#### Joining and Mapping:
- Converting the list of digits to an integer involves iterating through each digit once during the `map(str, digits)` operation and then joining them using `''.join(...)`.
- The time complexity for this part is O(N), where N is the length of the digits list.

#### Integer Addition and Conversion:
- The addition of 1 to the integer and the subsequent conversion of the result back to a list of digits are constant time operations.

#### Overall:
- The dominant factor in the time complexity is the O(N) operation for joining and mapping the digits.
- **Overall Time Complexity: O(N)**

### Space Complexity:
#### Integer Conversion:
- The space complexity is mainly influenced by the conversion of the list of digits to an integer, which creates a new string representation of the digits.
- The space required for the string representation is O(N), where N is the length of the digits list.

#### List Conversion:
- Converting the integer back to a list of digits also requires additional space for the string representation.
- The space for the string representation is O(N).

#### Result Variable:
- The result variable is used to store the intermediate integer, and its space complexity is O(N).

- **Overall Space Complexity: O(N)**

