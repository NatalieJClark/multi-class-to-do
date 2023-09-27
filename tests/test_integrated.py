from lib.todo_list import TodoList
from lib.todo import Todo

"""
Given a todo task
Its reflected in the todo list
"""
def test_given_single_task_incomplete_returns_task_after_adding():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_list.add(todo_1)
    assert todo_list.incomplete() == [todo_1]

"""
Given mulliple todo tasks
They are all reflected in the todo list
"""
def test_given_multiple_tasks_incomplete_returns_all_tasks_after_adding():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Walk the frog")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]

"""
Given multiple todo tasks
And one is marked complete
#incomplete returns the incompleted tasks
#complete returns the completed tasks
"""
def test_todo_marked_completed_reflected_in_complete_and_removed_from_incomplete():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Walk the frog")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_2.mark_complete()
    assert todo_list.incomplete() == [todo_1]
    assert todo_list.complete() == [todo_2]

"""
Given multiple todo tasks
and we call #give_up 
#incomplete returns []
#complete returns all tasks
"""
def test_after_give_up_incomplete_returns_empty_list_and_complete_lists_all():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Walk the frog")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo_1, todo_2]