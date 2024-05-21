# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function to print the Fibonacci sequence up to a given number of terms
def fibonacci(n):
    a, b = 0, 1
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

# Main program
print("Welcome to the program!")
choice = input("Enter 1 to calculate a factorial, or 2 to print the Fibonacci sequence: ")

if choice == "1":
    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
elif choice == "2":
    terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    fibonacci(terms)
else:
    print("Invalid choice!")