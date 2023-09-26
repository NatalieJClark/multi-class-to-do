```python
"""
integrated tests:
"""

"""
Given a todo task
Its reflected in the todo list
"""
todo_list = TodoList()
todo_1 = Todo("Walk the dog")
todo_list.add(todo_1)
todo_list.incomplete() #=> [todo_1]

"""
Given multiple todo tasks
And one is marked complete
#incomplete returns the incompleted tasks
#complete returns the completed tasks
"""
todo_list = TodoList()
todo_1 = Todo("Walk the dog")
todo_2 = Todo("Walk the frog")
todo_list.add(todo_1)
todo_list.add(todo_2)
todo_2.mark_complete()
todo_list.incomplete() #=> [todo_1]
todo_list.complete() #=> [todo_2]


"""
Given multiple todo tasks
and we call #give_up 
#incomplete returns []
#complete returns all tasks
"""
todo_list = TodoList()
todo_1 = Todo("Walk the dog")
todo_2 = Todo("Walk the frog")
todo_list.add(todo_1)
todo_list.add(todo_2)
todo_list.give_up()
todo_list.incomplete() #=> []
todo_list.complete() #=> [todo_1, todo_2]

===================================

"""
unit test todo_list
"""

"""
Given todo that is not an instance of todo class
#add Raises an error
"""
todo_list = TodoList()
todo_list.add("task_1")
# raises error "To do must be an instance of Todo class



===================================

"""
unit test todo
"""

"""
If we initialise with a task
We can get the task and complete back
"""
task_1 = Todo("Walk the dog")
task_1.task #=> "Walk the dog"
task_1.complete #=> False

"""
Given an empty string
Raises an error
"""
task_1 = Todo("")
# raises error "Task cannot be empty"

"""
Given an integer
Raises an error
"""
task_1 = Todo(2)
# raises error "Task cannot be an integer"


"""
Given a task
If you run #mark_complete on this task
We get complete back as True for that task
"""
task_1 = Todo("Walk the dog")
task_1.mark_complete()
task_1.complete #=> True


```