# Python Factorial Program

A simple Python program to calculate the factorial of a given number. The program also handles important cases such as zero and negative numbers.

##  Description

The factorial of a positive integer `n` is the product of all positive integers from `1` to `n`.

### Formula

```text
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

For example:

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

##  Source Code

```python
# Python program to find factorial of a number

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0:
    print("Factorial of 0 is 1.")

else:
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial of", num, "is", fact)
```

##  How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-repository-url>
```

### 3. Open the Repository

```bash
cd <repository-name>
```

### 4. Run the Program

```bash
python factorial.py
```

On some systems, you can use:

```bash
py factorial.py
```

##  Sample Test Cases

### Positive Number

```text
Enter a number: 5
Factorial of 5 is 120
```

### Zero

```text
Enter a number: 0
Factorial of 0 is 1.
```

### Negative Number

```text
Enter a number: -4
Factorial is not defined for negative numbers.
```

##  Concepts Used

* Python variables
* `input()` function
* `int()` conversion
* `if-elif-else`
* `for` loop
* Arithmetic operators
* Factorial calculation

##  Possible Cases

| Input           | Result                    |
| --------------- | ------------------------- |
| Positive number | Calculates factorial      |
| `0`             | Returns `1`               |
| Negative number | Displays an error message |

##  Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

## Author

**SARATHY S**

---

⭐ If you find this project useful, consider giving the repository a star!
