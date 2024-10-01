def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def remove_task(tasks):
    choice = input("Remove by (1) name or (2) index? ")
    if choice == "1":
        task_name = input("Enter the task name: ")
        if task_name in tasks:
            tasks.remove(task_name)
            print("Task removed successfully!")
        else:
            print("Task not found.")
    elif choice == "2":
        try:
            index = int(input("Enter the task index: "))
            if 1 <= index <= len(tasks):
                del tasks[index - 1]
                print("Task removed successfully!")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

def mark_task_status(tasks):
    choice = input("Mark task as (1) completed or (2) pending? ")
    if choice == "1":
        task_name = input("Enter the task name: ")
        if task_name in tasks:
            tasks.remove(task_name)
            tasks.append(f"✅ {task_name}")
            print("Task marked as completed.")
        else:
            print("Task not found.")
    elif choice == "2":
        task_name = input("Enter the task name: ")
        if task_name in tasks:
            tasks.remove(task_name)
            tasks.append(f"❌ {task_name}")
            print("Task marked as pending.")
        else:
            print("Task not found.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Remove task")
        print("4. Mark task status")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_task_status(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if _name_ == "_main_":
    main()