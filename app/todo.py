from storage import load_tasks, save_tasks

class TodoApp:
  def __init__(self):
    self.tasks = load_tasks()

 def add_task(self, task):
    new_task = {
        "text": task,
        "done": False
    }
    self.tasks.append(new_task)
    save_tasks(self.tasks)

def delete_task(self, index):
    try:
        removed = self.tasks.pop(index)
        save_tasks(self.tasks)
        print(f"Deleted: {removed}")
    except IndexError:
        print("Invalid task number")
    
    def ```python id="h4v8xg"
def show_tasks(self):
    if not self.tasks:
        print("\nNo tasks yet")
        return

    print("\nTasks:")
    for i, t in enumerate(self.tasks, 1):
    status = "✔" if t["done"] else "✘"
    print(f"{i}. [{status}] {t['text']}")

    def run(self):
    while True:
print("1. Add task")
print("2. Show tasks")
print("3. Mark as done")
print("4. Delete task")
print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            task = input("Enter task: ")
            self.add_task(task)

        elif choice == "2":
            self.show_tasks()

     elif choice == "3":
    if not self.tasks:
        print("No tasks to delete")
        continue

    self.show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        self.delete_task(index)
    except ValueError:
        print("Please enter a valid number")

elif choice == "4":
    break

        else:
            print("Invalid choice")

def mark_done(self, index):
    try:
        self.tasks[index]["done"] = True
        save_tasks(self.tasks)
        print("Task marked as done")
    except IndexError:
        print("Invalid task number")


elif choice == "3":
    if not self.tasks:
        print("No tasks to update")
        continue

    self.show_tasks()
    try:
        index = int(input("Enter task number: ")) - 1
        self.mark_done(index)
    except ValueError:
        print("Invalid input")

elif choice == "4":
    # delete логика (оставь как есть)

elif choice == "5":
    break
