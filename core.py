def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Task name: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Added: {title}")
    else:
        print("Task name cannot be empty!")

def mark_done(tasks):
    if not tasks:
        print("No tasks to mark done!")
        return
    
    show_tasks(tasks)
    try:
        idx = int(input("Task number: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print(f"Marked done: {tasks[idx]['title']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete!")
        return
    
    show_tasks(tasks)
    try:
        idx = int(input("Task number: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")