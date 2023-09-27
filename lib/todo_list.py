from lib.todo import Todo

class TodoList:
    def __init__(self):
        self._todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if isinstance(todo, Todo) == False:
            raise Exception("To do must be an instance of Todo class")
        self._todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete = list(filter(lambda todo : todo.complete != True, self._todo_list))
        return incomplete

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete = list(filter(lambda todo : todo.complete == True, self._todo_list))
        return complete

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self._todo_list:
            todo.mark_complete()