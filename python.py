# Get input from the user
print("Welcome Please")
num1 = float(input("Enter your first number: "))
print("Your first number is :", num1)
num2 = float(input("Enter your second number: "))
print("Your second number is :", num2)
operation = input("Now Enter the operation (+, -, *, /): ").lower()
print("Your selected operation is :", operation)

# Perform the operation based on user input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed!"
else:
    result = "Invalid operation!"

# Print the result
print(f"The result of {num1} {operation} {num22} is: {result}")
