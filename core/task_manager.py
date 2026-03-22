import json
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.file = "data/db.json"
        self.tasks = self.load()

    def load(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, course, desc, deadline, priority):
        task = {
            "course": course,
            "desc": desc,
            "deadline": deadline,
            "priority": priority,
            "done": False
        }
        self.tasks.append(task)
        self.save()

def get_urgent(self, days=2):
    today = datetime.now()
    urgent = []

    for t in self.tasks:
        try:
            d = datetime.strptime(t["deadline"], "%Y-%m-%d")
            if (d - today).days <= days and not t["done"]:
                urgent.append(t)
        except ValueError:
            print(f"Invalid date format in task: {t}")

    return urgent