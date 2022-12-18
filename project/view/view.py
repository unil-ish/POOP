class TaskView:
    def show(self, task):
        print(f'{task.title}: {task.description}')
        print(f'Completed: {task.completed}')
