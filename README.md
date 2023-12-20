# Multi Class To Do

## Introduction
- This is my repo for Makers Module 2 - Golden Square: Test Driving a Multi Class System
- This project was a challenge for this module section
- It contains a Todo class and a TodoList class, as well as unit and integration tests
- The user can create Todo objects and add them to a TodoList object
- The user can also:
  - mark a Todo object complete
  - list all the complete Todo instances in a TodoList object
  - list all the incomplete Todo instances in a TodoList object
  - "giveup" and mark all the Todo instances in a TodoList as complete
  
## Objectives
I used this project to learn how to:
- [x] Encapsulate state and behaviour as classes
- [x] Write unit tests for a multi-class program  
- [x] Write integration tests for a multi-class program

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# This will ensure you have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now install the latest Python.
; pyenv install 3.11

# Install pipenv
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version # Check pipenv is installed
pipenv, version ...
```
To test the practise code: 
```shell
# Install the dependencies (pytest)
; pipenv install # NB: you may need to change interpreters to import pytest

# Optionally ...
# Activate the project's virtualenv
; pipenv shell

# If using the pipenv shell:
# This runs all of the tests in the current directory
; pytest
# And this exits the pipenv shell
; exit # or Ctrl-D

# Otherwise, this runs all of the tests in the current directory
; pipenv run pytest
```
