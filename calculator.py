while True:
    print("Welcome to Smart Calculator")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation:")
    print("+  for Addition")
    print("-  for Subtraction")
    print("*  for Multiplication")
    print("/  for Division")
    print("** for Power")

    op = input("Enter operation: ")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            continue
        result = num1 / num2
    elif op == "":
        result = num1 ** num2
    else:
        print("Invalid operation!")
        continue

    print("Result =", result)

    print("Comparison between numbers:")
    if num1 > num2:
        print("num1 is greater than num2")
    elif num1 < num2:
        print("num1 is smaller than num2")
    else:
        print("Both numbers are equal")

    print("Number signs:")
    if num1 >= 0:
        print("num1 is Positive")
    else:
        print("num1 is Negative")

    if num2 >= 0:
        print("num2 is Positive")
    else:
        print("num2 is Negative")

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break