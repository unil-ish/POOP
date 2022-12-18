class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def mark_complete(self):
        self.model.mark_complete()
        self.view.show(self.model)
