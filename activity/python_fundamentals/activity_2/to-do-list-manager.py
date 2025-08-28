def read_file():
    with open("tasks.txt","r") as file:
        tasks = []
        lines = file.readlines()
        for task in lines:
            tasks.append(task.strip())
    return tasks

def write_file(new_task):
      with open("tasks.txt","a") as file:
                file.write(f"{new_task}\n")

def update_files(updated_task):
     with open("tasks.txt","w") as file:
          for task in updated_task:
               file.write(f"{task.strip()}\n")
     

print("To-Do List Menu")
print("1. View Tasks")
print("2. Add Tasks")
print("3. Remove Tasks")
print("4. Exit")



tasks = []
choice = 1
   
while choice != 4:
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
                task = read_file()
                if not task:
                     print("no task yet")
                else:
                    print("Tasks: ")
                    for i, task in enumerate(read_file(),start=1):
                        print(f"{i}. {task}")
                    print("\n")
        case 2:
            new_task = input("Enter new task: ")
            write_file(new_task)
            print("Task added!\n")

        case 3:
            updated_tasks = read_file()
            if not updated_tasks:
                 print("No task to remove.\n")
                 continue
        
            for i, task in enumerate(read_file(),start=1):
                    print(f"{i}. {task}")

            choice_delete = int(input("Enter task number to remove: "))
            if 1 <= choice_delete <= len(updated_tasks):
                del updated_tasks[choice_delete-1]
                update_files(updated_tasks)
                print("Task Removed!\n")
            else:
                print("invalid task number")

        case 4:
            print("Tasks saved. Goodbye!")
        case _:
            print("Invalid choice!\n")