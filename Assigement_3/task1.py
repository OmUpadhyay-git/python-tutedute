def factorial(n):
    """Calculate factorial using a loop"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main program
num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")