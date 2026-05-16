# ============================================================
# Safe Calculator (No-Crash Calculator)
# Knowledge Points: dictionary / lambda / try-except / while loop
# ============================================================

# ① Use a dictionary to map operators to their corresponding functions
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

print("Welcome to the Safe Calculator! Type 'quit' to exit.")
print(f"Supported operators: {' '.join(operations.keys())}")

# ② while True loop to continuously ask for user input until they choose to quit
while True:

    # ③ obtain the first number, and handle "non-numeric input"
    user_input = input("\nPlease enter the first number (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        print("👋 Goodbye!")
        break                      # jump out of the while loop, end the program

    try:
        num1 = float(user_input)   # try to convert to a number
    except ValueError:
        print("❌ Please enter a valid number!")
        continue                   # jump back to the top of the while loop

    # ④ obtain the operator, and check if it's in the dictionary
    op = input("Please enter the operator (+ - * /): ")
    if op not in operations:       # use in to check if the key exists in the dictionary
        print(f"❌ Unsupported operator: {op}")
        continue

    # ⑤ obtain the second number, and handle "non-numeric input"
    try:
        num2 = float(input("Please enter the second number: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    # ⑥ operate the calculation, separately handle "division by zero"
    try:
        func   = operations[op]    # from the dictionary, retrieve the corresponding function
        result = func(num1, num2)  # call the function
        print(f"✅ {num1} {op} {num2} = {result}")
    except ZeroDivisionError:
        print("❌ The divisor cannot be zero!")