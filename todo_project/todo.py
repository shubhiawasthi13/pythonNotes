import os 
TASKS_FILE = "todo_project/tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE,"r") as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully")

def display_tasks(tasks):
    if not tasks:
        print("no task added in todo list")
    else:
        print("\n ====To-Do list====")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}. {task}") 



def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("\n Enter task number to remove: "))
        if 1 <= task_index <=len(tasks):
            remove_task = tasks.pop(task_index - 1)
            save_tasks(tasks)
            print(f"Task '{remove_task}' removed successfully")
        else:
            print("Invalid task")   
    except ValueError:
        print("Please enter a valid number.") 

def main():
    tasks = load_tasks()    

    while True:
        print("\n ---To-Do List ---")
        print("1. Views tasks") 
        print("2. Add a tasks")  
        print("3. Remove a tasks")   
        print("4. Exit")  

        choice = input("Select an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks) 
        elif choice == "3":
            remove_task(tasks)  
        elif choice == "4":
            print("Good bye!")
            break
        else:
            print("Invaild option. Please try again.")

if __name__ == "__main__":
    main()
                                                                
