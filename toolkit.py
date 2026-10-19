# PLP Week 8: Personal Mini-Toolkit

tasks = []


# Tool 1: Add, view, and remove tasks.
def todo_manager():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an action (1-4): ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if tasks:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your task list is empty.")

        elif choice == "3":
            if tasks:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                try:
                    number = int(input("Enter task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Task removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a whole number.")
            else:
                print("There are no tasks to remove.")

        elif choice == "4":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


# Tool 2: Add, subtract, multiply, or divide numbers.
def simple_calculator():
    print("\n--- Simple Calculator ---")
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        operation = input("Choose +, -, *, or /: ").strip()

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            if second == 0:
                print("You cannot divide by zero.")
                return
            result = first / second
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result:g}")
    except ValueError:
        print("Please enter valid numbers.")


# Tool 3: Check whether a whole number is even or odd.
def even_odd_checker():
    print("\n--- Even and Odd Number Checker ---")
    try:
        number = int(input("Enter a whole number: "))
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    except ValueError:
        print("Please enter a valid whole number.")


# Main menu: Repeat until the user chooses Quit.
def main():
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n===== PERSONAL MINI-TOOLKIT =====")
        print("1. To-Do List Manager")
        print("2. Simple Calculator")
        print("3. Even and Odd Number Checker")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            todo_manager()
        elif choice == "2":
            simple_calculator()
        elif choice == "3":
            even_odd_checker()
        elif choice == "4":
            print("Thank you for using the toolkit. Goodbye!")
            break
        else:
            print("Sorry, that choice is invalid. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
