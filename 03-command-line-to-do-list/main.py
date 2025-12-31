def main():
    # 1. Create the list here. This will be our single source of truth.
    tasks = []

    while True:

        print("\n*****To Do List*****")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Exit")
         
        choice = input("Action: ")

        if choice == "1":
            # Pass the list to the function to be modified
            add_task(tasks)
        elif choice == "2":
            # Pass the list to the function to be displayed
            view_tasks(tasks)
        elif choice == "3":
            # Pass the list to the function to have an item removed
            complete_task(tasks)
        elif choice == "4":
            print("\nHave a good day!".title())
            break
        else:
            print("\nInvalid Action number! Please choose a number from 1 to 4.".title())

def add_task(task_list):
    """Asks for a task and adds it to the list."""
    print()
    new_task = input("Enter the description of the new task: ").strip()
    
    """
    This condition checks that `new_task` contains text.
    Empty strings are falsy in Python, so the `if` block
    runs only when the input is not empty.
    """
    if new_task: # Checks if the string is not empty

        # append() adds a new element to the end of the list.
        task_list.append(new_task)
        print(f"Task '{new_task}' added successfully.")
    else:
        print("Task description cannot be empty.")

def view_tasks(task_list):
    """Displays all tasks in the list."""
    print("\n--- Your Tasks ---")
    if not task_list: # Empty lists are falsy in Python
        print("Your to-do list is empty.")
    else:
        index = 1  # Start numbering from 1 (human-friendly)
        for task in task_list:
            print(f"{index}. {task}")
            index += 1  # Move to the next number
    print("------------------")

def complete_task(task_list):
    """Marks a task as complete by removing it from the list."""
    # First, show the user the tasks so they know which number to pick
    view_tasks(task_list)

    # Don't ask to complete a task if the list is empty
    if not task_list:
        return

    try:
        task_number = int(input("Enter the number of the task to complete: "))
        
        # We subtract 1 because our list is 0-indexed (starts at 0)
        # but we displayed it to the user starting from 1.
        task_index = task_number - 1

        # Validate the index
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index) # .pop() is a safe way to remove and get the item
            print(f"Task '{removed_task}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

main()
