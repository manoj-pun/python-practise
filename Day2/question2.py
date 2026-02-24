#Build a simple calculator that takes two numbers and an operator (+, -, *, /) from the user and performs the
#operation with proper division-by-zero handling.

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Choose the operator (+, -, *, /): ").strip()

        match operator:
            case "+":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            case "-":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            case "*":
                result = num1 * num2
                print(f"{num1} × {num2} = {result}")
            case "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue          # ← go back to start of loop
                result = num1 / num2
                print(f"{num1} ÷ {num2} = {result}")
            case _:
                print("Error: Invalid operator! Please use one of: +, -, *, /")
                continue              # ← go back to start of loop

        # If we reach here → calculation was successful
        break                         # ← exit the loop

    except ValueError:
        print("Error: Please enter valid numbers!")
        # no break → loop continues automatically
    except Exception as e:
        print(f"Unexpected error: {e}")
        # you can decide: continue or break
    

