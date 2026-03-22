class Dashboard:
    def __init__(self, tm, scheduler):
        self.tm = tm
        self.scheduler = scheduler

    def show_menu(self):
        print("\n=== STUDY OS ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Today's Plan")
        print("4. Exit")

        choice = input(">>> ")

        if choice == "1":
            self.add_task()
        elif choice == "2":
            self.show_tasks()
        elif choice == "3":
            self.show_plan()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")

    def add_task(self):
        course = input("Course: ")
        desc = input("Task: ")
        deadline = input("Deadline (YYYY-MM-DD): ")

        try:
            priority = int(input("Priority (1-5): "))
        except:
            print("Invalid priority, set to 3")
            priority = 3

        self.tm.add_task(course, desc, deadline, priority)
        print("✅ Task added!")

    def show_tasks(self):
        if not self.tm.tasks:
            print("No tasks.")
            return

        print("\n--- TASKS ---")
        for i, t in enumerate(self.tm.tasks):
            status = "DONE" if t["done"] else "TODO"
            print(f"{i}. [{status}] {t['course']} - {t['desc']} (Due: {t['deadline']})")

    def show_plan(self):
        tasks = self.scheduler.suggest_day_plan()

        if not tasks:
            print("No tasks for today 🎉")
            return

        print("\n--- TODAY'S PLAN ---")
        for t in tasks:
            print(f"{t['course']} - {t['desc']} (Due: {t['deadline']})")