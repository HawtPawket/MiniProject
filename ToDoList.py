# todo list app 
tasks = []

def new(title="Incomplete", priority="Low"):
    tasks.append({"title": title, "status": "Incomplete", "priority": priority,})
    print("Task added successfully.")

def view():
    for index, task in enumerate(tasks, start=1):
        
        print(f"{index}. {task['title']} - {task['status']} - Priority: {task['priority']}")

def completed():
    view()
    taskIndex = int(input("Enter the task number to mark as complete: ")) - 1
    try:
        taskIndex < 0 or taskIndex >= len(tasks)
        print("Invalid task number.")
    except ValueError:
            print("please enter the numerical value of the task")
    tasks[taskIndex]["status"] = "Complete"
    print("Task marked as complete.")
    return

def delete():
    view()
    taskIndex = int(input("Enter the task number to delete: ")) - 1
    if taskIndex < 0 or taskIndex >= len(tasks):
        print("Invalid task number.")
        return
    del tasks[taskIndex]
    print("Task deleted.")

def menu():
    print("""
    ***Welcome to the To-Do List!***
    ================================
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)

def main():

    while True:
        menu()
        choice = input("Enter your choice using 1-5: ")
       
        if choice == '1':
            title = input("Enter task: ")
            priority = input("Priority (Low/Medium/High/Urgent): ")
            
            new(title, priority)
        elif choice == '2':
            view()
        elif choice == '3':
            completed()
        elif choice == '4':
            delete()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the To-Do List")


if __name__ == "__main__":
    main()
