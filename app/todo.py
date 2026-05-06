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

    def edit_task(self, index, new_text):
        try:
            if not new_text.strip():
                print("Task cannot be empty")
                return

            old_text = self.tasks[index]["text"]
            self.tasks[index]["text"] = new_text
            save_tasks(self.tasks)
            print(f"Updated: {old_text} -> {new_text}")
        except IndexError:
            print("Invalid task number")

    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks yet")
            return

  title = "Completed tasks" if show_done else "Active tasks"
print(f"\n{title}:")
        for i, t in enumerate(self.tasks, 1):
            status = "✔" if t["done"] else "✘"
            print(f"{i}. [{status}] {t['text']}")

def filter_tasks(self, show_done=True):
    filtered = [t for t in self.tasks if t["done"] == show_done]

    if not filtered:
        print("\nNo tasks found")
        return

    print("\nFiltered tasks:")
    for i, t in enumerate(filtered, 1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. [{status}] {t['text']}")
    
    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            save_tasks(self.tasks)
            print(f"Deleted: {removed['text']}")
        except IndexError:
            print("Invalid task number")

    def mark_done(self, index):
        try:
            if self.tasks[index]["done"]:
                print("Task already completed")
                return

            self.tasks[index]["done"] = True
            save_tasks(self.tasks)
            print("Task marked as done")
        except IndexError:
            print("Invalid task number")

    def run(self):
        while True:
print("\n1. Add task")
print("2. Show tasks")
print("3. Mark as done")
print("4. Edit task")
print("5. Delete task")
print("6. Show completed")
print("7. Show active")
print("8. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                task = input("Enter new task: ")
                self.add_task(task)

            elif choice == "2":
                self.show_tasks()

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
                if not self.tasks:
                    print("No tasks to edit")
                    continue

                self.show_tasks()
                try:
                    index = int(input("Enter task number: ")) - 1
                    new_text = input("Enter new text: ")
                    self.edit_task(index, new_text)
                except ValueError:
                    print("Invalid input")

            elif choice == "5":
                if not self.tasks:
                    print("No tasks to delete")
                    continue
elif choice == "6":
    self.filter_tasks(show_done=True)

elif choice == "7":
    self.filter_tasks(show_done=False)
    elif choice == "8":
    break

                self.show_tasks()
                try:
                    index = int(input("Enter task number: ")) - 1
                    self.delete_task(index)
                except ValueError:
                    print("Please enter a valid number")

            elif choice == "6":
                break

            else:
                print("Invalid choice")
