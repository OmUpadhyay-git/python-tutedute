import math

a = float(input("Enter a number: "))

if a <= 0:
    print("Error: Number must be greater than 0.")
else:
    square_root = math.sqrt(a)
    logarithm = math.log(a)        
    sine_value = math.sin(a)       

    print(f"Square root: {square_root}")
    print(f"Logarithm: {logarithm}")
    print(f"Sine: {sine_value}")
