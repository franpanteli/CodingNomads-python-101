# Python-101-Introduction-to-Python

### Repository Overview
This repository contains my completed work for **[Python 101 - Introduction to Python](https://codingnomads.com/course/python-101-introduction-to-python)**, the first module in the **[Python Web Development Career Track](https://codingnomads.com/online-courses/python-bootcamp-web-development)** by [CodingNomads](https://codingnomads.com/).  

The course provided a comprehensive introduction to programming with [Python](https://www.python.org/), beginning with the fundamentals and progressing to practical projects.  

This repository reflects my independent learning journey, including:
- Lesson notes and exercises  
- Quizzes and challenges  
- [Projects](#projects-and-technical-exercises) (automation scripts & games)  
- [Technical Articles](#technical-articles)  

It demonstrates my progress in problem-solving, control flow, file automation, and interactive applications with Python.  

---

### Course Details
- **Course URL:** [Python 101 - Introduction to Python](https://codingnomads.com/course/python-101-introduction-to-python)  
- **Provider:** [CodingNomads](https://codingnomads.com/)  
- **Level:** Beginner → Intermediate foundations  
- **Duration:** ~75 hours (approx. 1 month at 15–20 hrs/week)  
- **Certificate:** [Python 101 Certificate of Completion](https://codingnomads.com/course/python-101-introduction-to-python)  

---

### Learning Objectives
This module equipped me with the following skills:

#### Python Fundamentals
- [Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator), [data types](https://docs.python.org/3/library/stdtypes.html) (`int`, `float`, `str`, `bool`)  
- [Operators](https://docs.python.org/3/library/operator.html), expressions, and type conversion  
- [Input](https://docs.python.org/3/library/functions.html#input) and [print](https://docs.python.org/3/library/functions.html#print)  

#### Control Flow
- [if / elif / else](https://docs.python.org/3/tutorial/controlflow.html#if-statements)  
- [Boolean logic](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)  
- [for loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements) & [while loops](https://docs.python.org/3/tutorial/controlflow.html#the-while-statement)  
- [break](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) / continue statements  

#### Functions
- [Defining](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) and [calling functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
- [Parameters](https://docs.python.org/3/glossary.html#term-parameter) and [return values](https://docs.python.org/3/reference/simple_stmts.html#return)  
- Variable [scope](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding)  

#### Data Structures
- [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), [tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences), [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), and [sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)  
- [Indexing & slicing](https://docs.python.org/3/tutorial/introduction.html#lists)  
- [Iteration](https://docs.python.org/3/tutorial/controlflow.html#for-statements)  

#### File Operations
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)  
- Using [`pathlib`](https://docs.python.org/3/library/pathlib.html) for cross-platform file handling  

#### Problem Solving
- Breaking down problems into steps  
- Writing clean, logical code  
- [Debugging](https://docs.python.org/3/library/pdb.html) and iterating  

---

### Projects and Technical Exercises
Here are the main projects I completed during this module:

---

#### [Screenshot Mover Script](https://github.com/franpanteli/CodingNomads-python-101/tree/main/codingnomads/projects/mover)
**Objective:** Automate the organization of `.png` files by moving them into a new subdirectory.  

- **Core concepts used:**  
  - [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) for directory management  
  - [`iterdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir) for iteration  
  - File filtering via [`suffix`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.suffix)  
  - File moving via [`rename()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rename)  
- **Article:** [How I Built a Screenshot Mover With Python](https://dev.to/fran_panteli/how-i-built-a-screenshot-mover-with-python-14i6)  
- **Source Code:** [mover.py](https://github.com/franpanteli/CodingNomads-python-101/blob/main/codingnomads/projects/mover/mover.py)  

---

#### [Text-Based Dungeons and Dragons Game](https://github.com/franpanteli/CodingNomads-python-101/blob/main/codingnomads/projects/dungeons_and_dragon_game.py/clirpg.py)
**Objective:** Build a text-based adventure game using Python fundamentals.  

- **Core concepts used:**  
  - [User input](https://docs.python.org/3/library/functions.html#input) & [string concatenation](https://docs.python.org/3/library/stdtypes.html#string-methods)  
  - [Conditional logic](https://docs.python.org/3/tutorial/controlflow.html#if-statements) for branching game outcomes  
  - [Booleans](https://docs.python.org/3/library/functions.html#bool) to track player state  
  - [Variables](https://docs.python.org/3/tutorial/introduction.html#numbers) for game conditions  
- **Article:** [How I Built a Dungeons and Dragons Game With Python](https://dev.to/fran_panteli/test-article-lig)  
- **Source Code:** [clirpg.py](https://github.com/franpanteli/CodingNomads-python-101/blob/main/codingnomads/projects/dungeons_and_dragon_game.py/clirpg.py)  

---

#### Mini-Projects & Exercises
Other exercises included:  
- [Guess My Number Game](https://github.com/franpanteli/CodingNomads-python-101/tree/main/codingnomads/projects) – random number guessing using [`random`](https://docs.python.org/3/library/random.html)  
- [Trip Cost Calculator](https://github.com/franpanteli/CodingNomads-python-101/tree/main/codingnomads/projects) – simple math operations & user input  
- [Hangman Game](https://github.com/franpanteli/CodingNomads-python-101/tree/main/codingnomads/projects) – iteration, loops, and conditionals  
- Function drills & loop practice exercises  

---

### Technical Articles
As part of the course, I wrote and published two technical tutorials on **[DEV Community](https://dev.to/)**:  

1. **[How I Built a Screenshot Mover With Python](https://dev.to/fran_panteli/how-i-built-a-screenshot-mover-with-python-14i6)**  
   - Walkthrough of my automation script with [`pathlib`](https://docs.python.org/3/library/pathlib.html)  
   - Discusses implementation, lessons learned, and improvements  

2. **[How I Built a Dungeons and Dragons Game With Python](https://dev.to/fran_panteli/test-article-lig)**  
   - Breakdown of a CLI-based game project  
   - Explains [user input](https://docs.python.org/3/library/functions.html#input), [conditionals](https://docs.python.org/3/tutorial/controlflow.html#if-statements), and [boolean states](https://docs.python.org/3/library/functions.html#bool)  
   - Includes ideas for extending the game with [Flask](https://flask.palletsprojects.com/) or [Django](https://www.djangoproject.com/)  

---

### Skills Gained
- Strong foundations in [Python syntax](https://docs.python.org/3/reference/) and program structure  
- Practical use of [functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements), [conditionals](https://docs.python.org/3/tutorial/controlflow.html#if-statements)  
- Built [automation scripts](https://dev.to/fran_panteli/how-i-built-a-screenshot-mover-with-python-14i6) and [interactive games](https://dev.to/fran_panteli/test-article-lig)  
- Improved technical writing through published tutorials  
- Prepared for upcoming modules in Python Web Development:  
  - [Flask](https://flask.palletsprojects.com/), [Django](https://www.djangoproject.com/), [APIs](https://realpython.com/api-integration-in-python/), [SQL](https://www.postgresql.org/)  

---

### To Clone This Repository
```bash
git clone https://github.com/franpanteli/Python-101-Introduction-to-Python.git
