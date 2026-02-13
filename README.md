# Experiment No. 7: Control Flow and Loops in Python

**Name:** Jayvee Shah  
**PRN:** 25070123058  
**Batch:** ENTC A3  

---

### I. Aim
To study and implement various control flow structures in the Python programming language, specifically focusing on conditional iterations using for and while loops, loop control statements (break, continue), and their applications in mathematical computations and multi-dimensional data processing.

---

### II. Theory

#### 1. Iteration Structures
* **The for Loop:** Used for iterating over a sequence (such as a list, string, or range). It is a "pre-test" loop where the number of iterations is generally predetermined by the length of the sequence or the range object.
* **The while Loop:** Executes a block of code as long as a specified Boolean condition remains True. This is ideal when the number of iterations is dependent on dynamic data processed during execution.

#### 2. Loop Control Keywords
* **break:** Terminates the current loop statement and transfers execution to the statement immediately following the loop.
* **continue:** Causes the loop to skip the remainder of its body and immediately retest its condition prior to beginning the next iteration.
* **else Clause:** Python allows an optional else block after a loop which executes only if the loop exited normally (i.e., not via a break statement).



#### 3. Nested Loops and Matrices
Nested loops are loops placed inside the body of another loop. This structure is the standard method for handling 2D arrays (matrices). For matrix multiplication, three nested loops are required to iterate through rows, columns, and the common dimension (dot product).

---

### III. Implementation Steps

1. **Sequence Generation:** Utilize the range(start, stop, step) function to generate numerical sequences for simple iterations and specific step-based increments.
2. **Mathematical Logic Implementation:**
    * **Factorial:** Initialize an accumulator to 1 and iteratively multiply it by every integer in the range [1, n].
    * **Fibonacci:** Maintain two variables, a and b. In each iteration, update them using tuple unpacking (a, b = b, a + b) to generate the next term in the sequence.
3. **Digit Manipulation:** * Extract the last digit of an integer using the modulo operator: digit = num % 10.
    * Reduce the number using floor division: num = num // 10.
4. **String Analysis:**
    * **Pointer Method:** Compare characters at index i and j (starting from opposite ends) using a while loop.
    * **Slicing Method:** Utilize [::-1] to create a reversed copy of the string for direct equality comparison.
5. **Matrix Operations:** Initialize 2D lists and use nested for loops to access elements. For multiplication, implement the dot product logic where result[i][j] is the sum of products of row elements of the first matrix and column elements of the second.



---

### IV. Summary of Operations

| Operation | Control Structure | Key Logic / Formula |
| :--- | :--- | :--- |
| Factorial | for loop | n! = 1 * 2 * 3 * ... * n |
| Fibonacci | for loop | a, b = b, a + b |
| Reverse Number | while loop | rev = (rev * 10) + (num % 10) |
| Palindrome | if-else / Slicing | string == string[::-1] |
| Matrix Product | Triple Nested for | result[i][j] += a[i][k] * b[k][j] |

---

### V. Conclusion
The experiment successfully demonstrated the versatility of Python's control flow. It was observed that while loops are superior for tasks involving unknown iteration counts, such as digit extraction or reversing numbers. for loops combined with range() provide a memory-efficient way to handle fixed numerical limits. Furthermore, the implementation of matrix multiplication highlighted the importance of nested loops in handling complex, multi-dimensional data structures.

---
