# Python-101-Introduction-to-Python

## Repository Overview
This repository contains my completed work for **[Python 101 - Introduction to Python](https://codingnomads.com/course/python-programming-101)**, the first module in the **[Python Web Development Career Track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp)** by [CodingNomads](https://codingnomads.com/).  

The course provided a comprehensive introduction to programming with Python, beginning with the fundamentals and progressing to practical projects.  

## Table of Contents
This repository reflects my independent learning journey, including:
- [Repository Overview](#repository-overview)
- [Course Details](#course-details)
- [Learning Objectives](#learning-objectives)
- [Projects and Technical Exercises](#projects-and-technical-exercises)
- [Technical Articles](#technical-articles)
- [Skills Gained](#skills-gained)
- [Clone This Repository](#to-clone-this-repository)

This shows my progress in problem-solving, control flow, file automation, and interactive applications with Python. 

---

## Course Details
- **Course URL:** [Python 101 - Introduction to Python](https://codingnomads.com/course/python-programming-101)  
- **Provider:** [CodingNomads](https://codingnomads.com/)  
- **Level:** Beginner → Intermediate foundations  
- **Duration:** ~75 hours (approx. 1 month at 15–20 hrs/week)  

---

## Learning Objectives
This module equipped me with the following skills:

### Python Fundamentals
- Variables, data types (`int`, `float`, `str`, `bool`)  
- Operators, expressions, and type conversion  
- Input and print  

### Control Flow
- if / elif / else statements  
- Boolean logic  
- for loops & while loops  
- break / continue statements  

### Functions
- Defining and calling functions  
- Parameters and return values  
- Variable scope  

### Data Structures
- Lists, tuples, dictionaries, and sets  
- Indexing & slicing  
- Iteration  

### File Operations
- Reading and writing files  
- Using `pathlib` for cross-platform file handling  

### Problem Solving
- Breaking down problems into steps  
- Writing clean, logical code  
- Debugging and iterating  

---

## Projects and Technical Exercises
Here are the main projects I completed during this module:

---

### [Screenshot Mover Script](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/mover/mover.py)
**Objective:** Automate the organisation of `.png` files by moving them into a new subdirectory.  

- **Core concepts used:**  
  - `pathlib.Path` for directory management  
  - `iterdir()` for iteration  
  - File filtering via `.suffix`  
  - File moving via `.rename()`  

---

### [Text-Based Dungeons and Dragons Game](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/dungeons_and_dragon_game.py/dungeons_and_dragon_game.py)
**Objective:** Build a text-based adventure game using Python fundamentals.  

- **Core concepts used:**  
  - User input & string concatenation  
  - Conditional logic for branching game outcomes  
  - Booleans to track player state  
  - Variables for game conditions  

---

### Mini-Projects & Exercises
Other exercises included:  
- [Guess My Number Game](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/resources/13_modules-and-automation/guess_the_number_game.py) – random number guessing using `random`  
- [Trip Cost Calculator](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/trip_cost_calculator/tip_cost_calculator.py) – simple math operations & user input  
- [Hangman Game](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/hangman/hangman.py) – iteration, loops, and conditionals  
- [Caesar Cipher](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/caesar_cipher/caesar_cipher.py) – encryption and string manipulation  
- [File Search Tool](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/filesearch/filesearch.py) – recursive file searching with `pathlib`  
- [Maze Maker](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/mazemaker/mazemaker.py) – programmatically generate mazes  
- [File Renamer](https://github.com/franpanteli/CodingNomads-python-101/blob/main/labs/projects/renamer/renamer.py) – batch file renaming with Python  

---

## Technical Articles

As part of this course, I wrote technical articles detailing some of my Python projects. These articles provide project walkthroughs, code explanations, and lessons learned.

### 1. [How I Built a Screenshot Mover With Python](https://dev.to/fran_panteli/how-i-built-a-screenshot-mover-with-python-14i6)
In this article, I explain how I automated file organisation by creating a Python script that moves `.png` files into a dedicated subdirectory. Key topics covered include:
- Using `pathlib.Path` for cross-platform file and directory manipulation
- Iterating through files with `iterdir()` and filtering by file extension
- Moving files using the `rename()` method
- Implementing basic automation to reduce manual file management
- Potential improvements such as handling multiple file types, adding command-line arguments, and logging

The article provides a step-by-step walkthrough, project structure, example code, and lessons learned from building the script.

### 2. [How I Built a Dungeons and Dragons Game With Python](https://dev.to/fran_panteli/test-article-lig)
This article describes the creation of a text-based adventure game inspired by Dungeons and Dragons. The game allows players to explore doors, pick up a sword, and face a dragon, demonstrating Python fundamentals. Key concepts discussed include:
- User input handling and string concatenation
- Conditional logic and branching with `if` statements
- Boolean variables to track game state
- Control flow for building interactive CLI-based applications
- Potential improvements, such as adding multiple rooms, health points, combat moves, inventory systems, loops for replayability, and even converting the game into a web application with Flask or Django

The article walks through the project’s code, explains its logic, and shares lessons learned while building an interactive game in Python.

---

## Skills Gained
- Strong foundations in Python syntax and program structure  
- Practical use of functions, loops, and conditionals  
- Built automation scripts and interactive games  
- Improved code organisation and debugging strategies  
- Prepared for upcoming modules in Python Web Development:  
  - Flask, Django, APIs, SQL  

---

## To Clone This Repository
```bash
git clone https://github.com/franpanteli/CodingNomads-python-101.git
