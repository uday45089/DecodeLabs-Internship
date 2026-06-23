tasks=[]
def add_task(task_name):
    task={"task":task_name}
    tasks.append(task)
    print(f"Task '{task_name}' added successfully.")
def view_tasks():
    if not tasks:
        print("No Tasks Available. Add a task to get started.")
    else:
        print("Tasks:")
        for index,task_name in enumerate(tasks,start=1):
            print(f"{index}. {task_name}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("Thank you for using the To-Do List!\nExiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":    main()