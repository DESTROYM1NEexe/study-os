class Analytics:
    def __init__(self, task_manager):
        self.tm = task_manager

    def completion_rate(self):
        tasks = self.tm.tasks
        if not tasks:
            return 0

        done = sum(1 for t in tasks if t["done"])
        return round(done / len(tasks) * 100, 2)