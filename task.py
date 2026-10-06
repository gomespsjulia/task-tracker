from datetime import datetime
import json
import sys

command = sys.argv[1]

if command == "add": 
    task = sys.argv[2]
    try:
        with open("task.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1
    now = datetime.now().isoformat() 
    new_task = {"id": new_id,
                "description": task,
                "status": "todo",
                "createdAt": now,
                "updatedAt": now}

    tasks.append(new_task)

    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)
      
    print("Task added:", task)

elif command == "list":
    try:
        with open("task.json", "r") as file:
            tasks = json.load(file)
        
    except FileNotFoundError:
            tasks = []
    if not tasks:
            print("You don't have any tasks yet.")
    else:
        print("Here are your tasks:")
        for task in tasks:
            print(f"{task['id']}. {task['description']} - {task['status']}")

elif command == "delete":
    try:
        task_id = int(sys.argv[2])
    except (ValueError, IndexError):
        print("Please provide a valid task ID.")
        sys.exit()

    try:
        with open("task.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        print("You don't have any tasks yet.")
        sys.exit()

    deleted = False
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            deleted = True
            break
    if deleted:
        with open("task.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print("Task deleted.")
    else:
        print("Task not found.")


