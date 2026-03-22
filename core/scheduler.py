class Scheduler:
    def __init__(self, task_manager):
        self.tm = task_manager

    def suggest_day_plan(self):
        tasks = sorted(
            self.tm.tasks,
            key=lambda x: (x["done"], x["priority"])
        )

        return [t for t in tasks if not t["done"]][:5]