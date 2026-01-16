# main.py
# Project: Deadline Control
# Author: Luana Andia da Costa

def show_menu():
    print("\n=== Deadline Control ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

def add_task(tasks):
    name = input("Task name: ")
    deadline = input("Deadline (dd/mm/yyyy): ")
    tasks.append({"name": name, "deadline": deadline, "status": "Pending"})
    print(f"Task '{name}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks registered.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} - Deadline: {task['deadline']} - Status: {task['status']}")

def main():
    tasks = []
    while True:
        show_menu()
        option = input("Choose an option: ")
        if option == "1":
            add_task(tasks)
        elif option == "2":
            view_tasks(tasks)
        elif option == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()