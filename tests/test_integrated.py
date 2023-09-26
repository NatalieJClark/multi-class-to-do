from lib.todo_list import TodoList
from lib.todo import Todo

"""
Given a todo task
Its reflected in the todo list
"""
def test_incomplete_returns_task_after_adding_task():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_list.add(todo_1)
    assert todo_list.incomplete() == [todo_1]

# """
# Given multiple todo tasks
# And one is marked complete
# #incomplete returns the incompleted tasks
# #complete returns the completed tasks
# """
# todo_list = TodoList()
# todo_1 = Todo("Walk the dog")
# todo_2 = Todo("Walk the frog")
# todo_list.add(todo_1)
# todo_list.add(todo_2)
# todo_2.mark_complete()
# todo_list.incomplete() #=> [todo_1]
# todo_list.complete() #=> [todo_2]


# """
# Given multiple todo tasks
# and we call #give_up 
# #incomplete returns []
# #complete returns all tasks
# """
# todo_list = TodoList()
# todo_1 = Todo("Walk the dog")
# todo_2 = Todo("Walk the frog")
# todo_list.add(todo_1)
# todo_list.add(todo_2)
# todo_list.give_up()
# todo_list.incomplete() #=> []
# todo_list.complete() #=> [todo_1, todo_2]