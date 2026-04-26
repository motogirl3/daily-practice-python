def add_task(tasks):
    task = input("Enter a task (or 'exit'): ")
    return task

def show_tasks(tasks):
    print("\nYour tasks:")
    for t in tasks:
        print("-", t)

tasks = []

while True:
    task = add_task(tasks)

    if task == "exit":
        break

    tasks.append(task)

show_tasks(tasks)
