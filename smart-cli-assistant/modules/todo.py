from pathlib import Path
import json

base_dir = Path(__file__).resolve().parent.parent
data_folder = base_dir / "data"
file_to_open = data_folder / "task.json"

def todo(command):
    if "add" in command or "added" in command:
        add_task()
    elif "remove" in command:
        remove_task()
    elif "show" in command:
        show_task()
    else:
        print("Unknown todo command. Use 'todo add' or 'todo remove'.")

def add_task():
    data_folder.mkdir(parents=True, exist_ok=True)
    tasks = []

    if file_to_open.exists():
        with open(file_to_open, mode='r', encoding='utf-8') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []

    value = input("Enter the task: ")
    next_id = 1
    if tasks:
        next_id = max(item.get("id", 0) for item in tasks) + 1

    tasks.append({"id": next_id, "name": value})

    with open(file_to_open, mode='w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)

    print(f"Task added with id {next_id}.")


def remove_task():
    if not file_to_open.exists():
        print("No task file found to remove from.")
        return

    with open(file_to_open, mode='r', encoding='utf-8') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            print("Task file is empty or invalid JSON.")
            return

    if not tasks:
        print("No tasks to remove.")
        return

    print("Existing tasks:")
    for item in tasks:
        print(f"{item.get('id')}: {item.get('name')}")

    task_id = input("Enter the id of the task to remove: ")
    updated = [item for item in tasks if str(item.get("id")) != task_id]

    if len(updated) == len(tasks):
        print(f"Task id {task_id} not found.")
        return

    with open(file_to_open, mode='w', encoding='utf-8') as file:
        json.dump(updated, file, indent=4)

    print(f"Task {task_id} removed.")

def show_task():
    data_folder.mkdir(parents=True, exist_ok=True)
    with open(file_to_open, mode='r', encoding='utf-8') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            print("Task file is empty or invalid JSON.")
            return
    for item in tasks:
        print(f"{item.get('id')}) {item.get('name')}")
    print()