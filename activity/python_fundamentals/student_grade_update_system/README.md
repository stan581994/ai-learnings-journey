### 1. 📝 Problem Title: **Student Grades Update System**

### **Problem Description**

You are tasked with creating a simple program to **store and update student grades** in a text file.  
The program should allow adding new students and updating grades for existing students while making sure the file always contains the latest data.

### **Requirements**

1. At the start, read the contents of `students.txt` (if it exists) and load them into a dictionary.
    
    - Keys = Student names
        
    - Values = Student grades
        
2. Ask the user how many students they want to enter.
    
3. For each student input:
    
    - If the student **already exists** in the dictionary → update the grade.
        
    - If the student **does not exist** → add them as a new entry.
        
4. After all inputs, **rewrite the file** (`students.txt`) with the updated dictionary.
    
5. Finally, display the updated list of all students and their grades
   
```yaml
File content before:
Alice:85
Bob:90

How many students? 2
Enter Student name: Alice
Enter Student grade: 95
Enter Student name: Charlie
Enter Student grade: 88

File content after:
Alice:95
Bob:90
Charlie:88

```

