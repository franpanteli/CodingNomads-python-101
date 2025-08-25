# Python-101-Introduction-to-Python

### Repository Overview
This repository contains my complete work for **Python 101 - Introduction to Python**, the first module in the **Python Web Development Career Track** by CodingNomads. The course provided a comprehensive introduction to programming with Python, starting from the very basics and gradually building towards practical applications and small projects. 

This repository reflects my independent learning journey through the course, including lesson notes, completed exercises, mini-projects, quizzes, and technical articles. It demonstrates my progress in thinking like a Python developer, solving problems programmatically, and applying Python concepts to real-world tasks.

---

### Course Details
- **Course URL:** [Python 101 - Introduction to Python](https://codingnomads.com/course/python-101-introduction-to-python)  
- **Provider:** CodingNomads  
- **Level:** Beginner  
- **Duration:** ~75 hours (~1 month at 15–20 hours per week)  
- **Certificate:** Python 101 Certificate  

---

### Learning Objectives
Through this course, I focused on developing the following skills:

1. **Python Fundamentals**
   - Variables and data types (integers, floats, strings, booleans)  
   - Operators, expressions, and order of operations  
   - Type conversion and casting  
   - User input and basic output formatting  

2. **Control Flow**
   - Conditional statements: `if`, `elif`, `else`  
   - Boolean logic and truthy/falsy values  
   - Looping constructs: `for` loops, `while` loops  
   - Break and continue statements  

3. **Functions**
   - Defining and calling functions  
   - Function parameters and return values  
   - Scope and lifetime of variables  
   - Using functions to organize code and improve reusability  

4. **Python Data Structures**
   - Lists, tuples, dictionaries, and sets  
   - Indexing, slicing, and iteration  
   - Common methods and operations for manipulating collections  

5. **File Operations**
   - Reading from and writing to files  
   - Automating file handling with Python scripts  
   - Using the `pathlib` module for cross-platform path manipulation  

6. **Problem-Solving and Algorithmic Thinking**
   - Breaking problems into smaller steps  
   - Using loops, conditionals, and functions to implement solutions  
   - Debugging code and iterating until correct behavior is achieved  

---

### Projects and Technical Exercises
During this module, I completed several projects that applied Python fundamentals in practical contexts. Each project includes a description, implementation highlights, and lessons learned.

#### 1. **Screenshot Mover Script**
- **Objective:** Automate the organization of `.png` files in a folder by moving them into a dedicated subdirectory.  
- **Key Features:**  
  - Iterates through files in a base directory using `pathlib.Path.iterdir()`  
  - Filters files based on `.png` extension  
  - Creates a new subdirectory if it doesn’t exist (`exist_ok=True`)  
  - Moves `.png` files to the new directory using `file.rename()`  
- **Concepts Practiced:**  
  - Path manipulation and object-oriented filesystem handling  
  - Conditional filtering and iteration  
  - File system automation  
- **Lessons Learned:**  
  - Automating repetitive tasks improves productivity  
  - The importance of cross-platform path handling  
  - Using Python scripts for practical file management  
- **Article:** [How I Built a Screenshot Mover With Python](https://dev.to/fran_panteli/how-i-built-a-screenshot-mover-with-python-14i6)  
- **Source Code:** [GitHub Repository](https://github.com/franpanteli/CodingNomads-python-101/tree/main/codingnomads/projects/mover)

#### 2. **Text-Based Dungeons and Dragons Game**
- **Objective:** Build an interactive, text-based adventure game inspired by Dungeons and Dragons, focusing on Python fundamentals.  
- **Key Features:**  
  - User enters their name and is greeted  
  - Player chooses between doors, facing challenges such as a dragon or finding a sword  
  - Boolean variables track player progress and determine game outcomes  
  - Nested conditional logic guides the story and user interactions  
- **Concepts Practiced:**  
  - User input and string handling  
  - Conditional statements and control flow  
  - Boolean state management  
  - Game logic implementation  
- **Lessons Learned:**  
  - Building interactive applications using Python fundamentals  
  - Importance of planning control flow for multiple user outcomes  
  - Structuring code for readability and logical progression  
- **Potential Improvements:**  
  - Adding multiple rooms, combat mechanics, and a health point system  
  - Introducing inventory management  
  - Modularizing code with functions  
  - Converting CLI game into a web application using Flask or Django  
- **Article:** [How I Built a Dungeons and Dragons Game With Python](https://dev.to/fran_panteli/test-article-lig)  
- **Source Code:** [GitHub Repository](https://github.com/franpanteli/CodingNomads-python-101/blob/main/codingnomads/projects/dungeons_and_dragon_game.py/clirpg.py)

#### 3. **Mini-Projects and Exercises**
- Completed smaller exercises to reinforce Python basics, such as:  
  - `Guess My Number` – random number guessing game  
  - `Trip Cost Calculator` – calculate expenses for a trip  
  - `Hangman` – classic word guessing game  
  - Function and loop practice problems  

These exercises strengthened my problem-solving skills and prepared me for more advanced topics in Python Web Development.

---

### Learning Highlights and Skills Gained
- Developed strong foundational Python skills and confidence with programming logic  
- Built automation scripts and interactive CLI applications  
- Learned to structure code cleanly using functions and conditionals  
- Applied problem-solving techniques to real-world tasks  
- Practiced writing technical articles to explain projects, enhancing communication skills  
- Prepared for further modules in **Python Web Development Career Track**, including Flask, Django, SQL, APIs, and object-oriented programming  

---

### To Clone This Repository
```bash
git clone https://github.com/franpanteli/Python-101-Introduction-to-Python.git
