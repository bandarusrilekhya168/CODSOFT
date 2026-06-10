# =====================================
# CODSOFT Python Internship
# Task 1 - To-Do List Application
# =====================================

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task name: ")
    tasks.append(task)
    print("✅ Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("📋 No tasks available.")
    else:
        print("\n📋 Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to update: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter new task name: ")
            tasks[task_number - 1] = new_task
            print("✅ Task updated successfully!")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"✅ '{deleted_task}' deleted successfully!")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

print("=================================")
print("      TO-DO LIST APPLICATION")
print("=================================")

while True:
    show_menu()

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using To-Do List App.")
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice. Please select between 1 and 5.")
