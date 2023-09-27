from lib.todo import Todo
import pytest

"""
If we initialise with a task
We can get the task and complete properties back
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
Given a task which is an integer
Raises an error
"""
def test_integer_raises_error():
    with pytest.raises(Exception) as e:
        task_1 = Todo(2)
    assert str(e.value) == "Task must be a string"

"""
Given a task which is a float
Raises an error
"""
def test_float_raises_error():
    with pytest.raises(Exception) as e:
        task_1 = Todo(5.5)
    assert str(e.value) == "Task must be a string"

"""
Given a task which is None
Raises an error
"""
def test_none_raises_error():
    with pytest.raises(Exception) as e:
        task_1 = Todo(None)
    assert str(e.value) == "Task must be a string"

"""
Given a task which is a boolean
Raises an error
"""
def test_boolean_raises_error():
    with pytest.raises(Exception) as e:
        task_1 = Todo(False)
    assert str(e.value) == "Task must be a string"

"""
Given a task
If you run #mark_complete on this task
We get complete property back as True for that task
"""
def test_task_mark_complete_get_true_back():
    task_1 = Todo("Walk the dog")
    task_1.mark_complete()
    assert task_1.complete == True

