# Daily Study Planner Application

DATA_FILE = "study_plans.txt"

def read_plans():
    try:
        with open(DATA_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def write_plans(plans):
    with open(DATA_FILE, "w") as f:
        for plan in plans:
            f.write(plan + "\n")

def show_plans(plans):
    if len(plans) == 0:
        print("No study plans added yet ❌")
    else:
        print("\nToday's Study Plans:")
        for i in range(len(plans)):
            print(f"{i+1}. {plans[i]}")

def add_plan(plans):
    plan = input("Enter your study plan: ")
    plans.append(plan)
    write_plans(plans)
    print("Study plan added successfully ✅")

def complete_plan(plans):
    show_plans(plans)
    if plans:
        try:
            num = int(input("Enter completed plan number: "))
            if 1 <= num <= len(plans):
                finished = plans.pop(num - 1)
                write_plans(plans)
                print(f"Study plan '{finished}' completed 🎉")
            else:
                print("Invalid number ❌")
        except ValueError:
            print("Please enter a valid number ❌")

def main():
    plans = read_plans()

    while True:
        print("\n--- DAILY STUDY PLANNER ---")
        print("1. Add Study Plan")
        print("2. View Study Plans")
        print("3. Mark Plan as Completed")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_plan(plans)
        elif choice == "2":
            show_plans(plans)
        elif choice == "3":
            complete_plan(plans)
        elif choice == "4":
            print("Planner closed. Happy Learning 📘")
            break
        else:
            print("Invalid choice ❌")

main()