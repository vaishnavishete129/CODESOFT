import math

def advanced_calculator():
    print("🔢 Welcome to the Advanced Calculator!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^ or **)")
        print("6. Square Root (√)")
        print("7. Modulus (%)")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Thanks for using the calculator. Goodbye!")
            break

        # Square root needs only one number
        if choice == '6':
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot take square root of a negative number.")
            else:
                print(f"Result: √{num} = {math.sqrt(num)}")

        # For other operations, take two inputs
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {math.pow(num1, num2)}")
            elif choice == '7':
                print(f"{num1} % {num2} = {num1 % num2}")
            else:
                print("Invalid choice! Try again.")

# Run the advanced calculator
advanced_calculator()
