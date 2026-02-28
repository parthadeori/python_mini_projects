# 8. Simple To-Do List

tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ADD TASK
    if choice == "1":
        task_name = input("Enter new task: ")
        tasks.append({"task": task_name, "done": False})
        print("Task added successfully!")

    # VIEW TASKS
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks):
                status = "✔" if task["done"] else "✘"
                print(f"{index + 1}. {task['task']} [{status}]")

    # REMOVE TASK
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['task']}")

            try:
                number = int(input("Enter task number to remove: "))
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"Removed: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # MARK COMPLETE
    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(tasks):
                status = "✔" if task["done"] else "✘"
                print(f"{index + 1}. {task['task']} [{status}]")

            try:
                number = int(input("Enter task number to mark complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # EXIT
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
