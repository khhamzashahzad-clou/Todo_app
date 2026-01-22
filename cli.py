from src.core import show_tasks, add_task, mark_done, delete_task
from src.storage import load_tasks, save_tasks

def run_cli():
    tasks = load_tasks()

    while True:
        print("""
=== Todo List CLI ===
1) Show Tasks
2) Add Task
3) Mark Task Done
4) Delete Task
5) Exit
        """)

        choice = input("Pick an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
