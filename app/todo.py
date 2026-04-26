class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        print("\nTasks:")
        for t in self.tasks:
            print("-", t)

    def run(self):
        while True:
            task = input("Enter task (or 'exit'): ")

            if task == "exit":
                break

            self.add_task(task)

        self.show_tasks()
