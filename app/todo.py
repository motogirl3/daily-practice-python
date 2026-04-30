from storage import load_tasks, save_tasks

class TodoApp:
  def __init__(self):
    self.tasks = load_tasks()

  def add_task(self, task):
    self.tasks.append(task)
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
        print(f"{i}. {t}")

    def run(self):
    while True:
       print("\n1. Add task")
print("2. Show tasks")
print("3. Delete task")
print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            task = input("Enter task: ")
            self.add_task(task)

        elif choice == "2":
            self.show_tasks()

       elif choice == "3":
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
