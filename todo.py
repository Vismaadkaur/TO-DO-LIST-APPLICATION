import os
import json
from datetime import datetime

# Add a new task with description, due date, and category
def add_new_task(task_list, task_desc, task_due_date, task_category):
    task_list.append({
        "description": task_desc,
        "due_date": task_due_date,
        "category": task_category,
        "completed": False
    })
    print("Task added successfully.")

# View all tasks, optionally showing completed ones
def display_tasks(task_list, show_completed=False):
    if not task_list:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(task_list, start=1):
            status = "Completed" if task['completed'] else "Pending"
            if show_completed or not task['completed']:
                print(f"{idx}. [{status}] {task['description']} - Due Date: {task['due_date']} - Category: {task['category']}")

# Remove a task by its index
def remove_task(task_list, task_idx):
    if 1 <= task_idx <= len(task_list):
        del task_list[task_idx - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task index. Please try again.")

# Mark a task as completed by its index
def mark_task_as_completed(task_list, task_idx):
    if 1 <= task_idx <= len(task_list):
        task_list[task_idx - 1]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index. Please try again.")

# Save the task list to a JSON file
def save_tasks(task_list, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(task_list, f, indent=4)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks to file: {e}")

# Load the task list from a JSON file
def load_tasks(file_path):
    task_list = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                task_list = json.load(f)
            print("Tasks loaded successfully.")
        except Exception as e:
            print(f"Error loading tasks from file: {e}")
    return task_list

# Validate the date input to ensure it follows the format YYYY-MM-DD
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Main application loop
def main():
    task_list = []
    file_path = "tasks.json"

    # Load existing tasks from file (if available)
    task_list = load_tasks(file_path)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            # Get task details from user
            task_desc = input("Enter task description: ")
            
            # Validate due date format
            while True:
                task_due_date = input("Enter due date (YYYY-MM-DD): ")
                if validate_date(task_due_date):
                    break
                else:
                    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            
            task_category = input("Enter task category (e.g., Work, Personal, Urgent): ")
            
            # Add task and save
            add_new_task(task_list, task_desc, task_due_date, task_category)
            save_tasks(task_list, file_path)
        
        elif choice == '2':
            # Display tasks with option to show completed ones
            show_completed = input("Show completed tasks? (y/n): ").lower() == 'y'
            display_tasks(task_list, show_completed)
        
        elif choice == '3':
            # Delete a task by index
            display_tasks(task_list)
            try:
                task_idx = int(input("Enter the task index to delete: "))
                remove_task(task_list, task_idx)
                save_tasks(task_list, file_path)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == '4':
            # Mark a task as completed by index
            display_tasks(task_list)
            try:
                task_idx = int(input("Enter the task index to mark as completed: "))
                mark_task_as_completed(task_list, task_idx)
                save_tasks(task_list, file_path)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == '5':
            # Exit the program
            print("Exiting the To-Do List Application.")
            break
        
        else:
            # Handle invalid menu options
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
