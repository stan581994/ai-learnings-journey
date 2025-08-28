# 📝 Python Programming Activity: To-Do List Manager  

## 🎯 Objective  
Enhance your Python skills by building a simple **To-Do List Manager** that stores tasks in a file and allows the user to interact with them through a menu system.  

---

## 📌 Instructions  

1. **File Setup**  
   - Create a file named `todo.txt`.  
   - Each line in the file represents one task.  

2. **Program Requirements**  
   - When the program starts, it should read the tasks from `todo.txt`.  
   - Display a menu with the following options:  
     ```
     1. View tasks
     2. Add task
     3. Remove task
     4. Exit
     ```  
   - The program should keep running until the user chooses **Exit**.  

3. **Features**  
   - **View tasks** → Display all tasks with numbers.  
   - **Add task** → Ask the user to type a new task, then add it to the list.  
   - **Remove task** → Ask for a task number, then remove it (with input validation).  
   - **Exit** → Save all tasks back to `todo.txt` and end the program.  

4. **Validation**  
   - If the user enters something that isn’t a number when required, show an error and ask again.  
   - If the task number does not exist when removing, show an error message.  

---

## 🖥 Example Program Run  

   
```yaml

To-Do List Menu

View tasks

Add task

Remove task

Exit

Choose an option: 1
Tasks:

Buy groceries

Finish Python homework

Choose an option: 2
Enter new task: Wash the car
Task added!

Choose an option: 3
Enter task number to remove: 1
Task removed!

Choose an option: 4
Tasks saved. Goodbye!

```