
💻 Project 3: The Command-Line To-Do List Manager
Your task is to create a program that allows a user to manage a simple to-do list directly from the command line.

Core Requirements:
Initial State: The program must start with an empty to-do list.

Main Menu: The program must run in a continuous loop that presents the user with the following options:

Add a new task

View all tasks

Mark a task as complete

Exit

Functionality & Behavioral Expectations:
Add Task:

This option should prompt the user for a description of the new task.

The task should be added to the list.

The program must not allow an empty or blank task description to be added.

View Tasks:

This option should display all the tasks currently on the list.

Each task must be numbered, starting from 1 (e.g., 1. Buy groceries, 2. Finish CS50 project).

If there are no tasks on the list, it should print a message like "Your to-do list is empty."

Mark Task as Complete:

This option should first display all the tasks with their numbers, just like the "View Tasks" option.

It should then ask the user to enter the number of the task they wish to complete.

The corresponding task should be removed from the list.

The program must handle invalid input. If the user enters a non-numeric value or a number that does not correspond to a task on the list (e.g., too high, too low, or zero), it should display an error message and not alter the list.

Exit:

This option should terminate the program with a friendly goodbye message.

Code Structure:

Your code must be well-structured and organized into functions (e.g., a main function, a function to add_task, a function to view_tasks, etc.).

Good luck. Take your time to plan out how you will store the tasks and how each function will interact with your list.

