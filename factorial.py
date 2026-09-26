# Python program to find factorial of a number

num = int(input("Enter a number: "))

# Case 1: Negative number
if num < 0:
    print("Factorial is not defined for negative numbers.")

# Case 2: Zero
elif num == 0:
    print("Factorial of 0 is 1.")

# Case 3: Positive number
else:
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial of", num, "is", fact)
