def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\nYour tasks:")
    for t in tasks:
        print("-", t)

tasks = load_tasks()

while True:
    task = input("Enter task (or 'exit'): ")

    if task == "exit":
        break

    tasks.append(task)
    save_tasks(tasks)

show_tasks(tasks)
