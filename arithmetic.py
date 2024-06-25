num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
if num2 != 0:
    div = num1 / num2
    mod = num1 % num2
else:
    div = "Undefined (division by zero)"
    mod = "Undefined (division by zero)"

print(f"\nArithmetic operations on {num1} and {num2}:")
print(f"1. Addition: {add}")
print(f"2. Subtraction: {sub}")
print(f"3. Multiplication: {mul}")
print(f"4. Division: {div}")
print(f"5. Modulus : {mod}")
