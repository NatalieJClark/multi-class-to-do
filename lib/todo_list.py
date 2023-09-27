from lib.todo import Todo

class TodoList:
    def __init__(self):
        self._todo_list = []
        self._incomplete_list = []
        self._complete_list = []

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
        for todo in self._todo_list:
            if todo.complete == False:
                self._incomplete_list.append(todo)
        return self._incomplete_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        for todo in self._todo_list:
            if todo.complete == True:
                self._complete_list.append(todo)
        return self._complete_list

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self._todo_list:
            todo.mark_complete()