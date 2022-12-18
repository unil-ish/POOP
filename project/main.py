# main.py
from project.controller.controller import TaskController
from project.model.model import Task
from project.view.view import TaskView

if __name__ == "__main__":
    # Create a task
    task = Task('Do homework', 'Complete math and science assignments')

    # Create a view to show the task
    task_view = TaskView()

    # Create a controller to mark the task as complete
    task_controller = TaskController(task, task_view)

    # Mark the task as complete
    task_controller.mark_complete()
