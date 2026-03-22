from core.scheduler import Scheduler
from core.task_manager import TaskManager
from ui.dashboard import Dashboard

tm = TaskManager()
scheduler = Scheduler(tm)
ui = Dashboard(tm, scheduler)

def main():
    while True:
        ui.show_menu()

if __name__ == "__main__":
    main()