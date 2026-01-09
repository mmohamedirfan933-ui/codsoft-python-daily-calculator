# Daily Calculator Application

def show_menu():
    print("\n--- DAILY CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Cannot divide by zero ❌")
        return None

while True:
    show_menu()
    choice = input("Choose option (1-5): ")

    if choice == "5":
        print("Calculator closed. Keep calculating 💡")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter a number ❌")
        continue

    if choice == "1":
        print("Result =", add(num1, num2))
    elif choice == "2":
        print("Result =", subtract(num1, num2))
    elif choice == "3":
        print("Result =", multiply(num1, num2))
    elif choice == "4":
        result = divide(num1, num2)
        if result is not None:
            print("Result =", result)
    else:
        print("Invalid choice ❌")