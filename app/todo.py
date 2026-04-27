from storage import load_tasks, save_tasks

class TodoApp:
  def __init__(self):
    self.tasks = load_tasks()

  def add_task(self, task):
    self.tasks.append(task)
    save_tasks(self.tasks)

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
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            task = input("Enter task: ")
            self.add_task(task)

        elif choice == "2":
            self.show_tasks()

        elif choice == "3":
            break

        else:
            print("Invalid choice")
