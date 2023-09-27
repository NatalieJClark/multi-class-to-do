from lib.todo_list import TodoList
import pytest

"""
If we initialise a to do list without adding a task
We can get the todo_list, incomplete_list and complete_list back as empty lists
"""
def test_initialising_todo_list():
    todo_list = TodoList()
    assert todo_list._todo_list == []

"""
Given todo that is not an instance of todo class
#add Raises an error
"""
def test_todo_not_instance_of_todo_raises_error():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.add("task_1")
    assert str(e.value) == "To do must be an instance of Todo class"