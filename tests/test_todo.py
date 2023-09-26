from lib.todo import Todo
import pytest

"""
If we initialise with a task
We can get the task and complete back
"""
def test_initialising_task():
    task_1 = Todo("Walk the dog")
    assert task_1.task == "Walk the dog"
    assert task_1.complete == False

"""
Given an empty string
Raises an error
"""
def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        task_1 = Todo("")
    assert str(e.value) == "Task cannot be empty"

"""
Given an integer
Raises an error
"""
def test_integer_raises_error():
    with pytest.raises(Exception) as e:
        task_1 = Todo(2)
    assert str(e.value) == "Task must be a string"


# """
# Given a task
# If you run #mark_complete on this task
# We get complete back as True for that task
# """
# task_1 = Todo("Walk the dog")
# task_1.mark_complete()
# task_1.complete #=> True

