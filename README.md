<h1 style="color: white; font-weight: normal; text-align: center; background: repeating-linear-gradient(45deg, #F22 0%, #F22 5%, #822 5%, #822 10%); margin: 32px 0; padding: 8px 0; text-shadow: #0004 0px 2px; border-radius: 4px; border: solid 1px #422;" ><b>HEAVILY</b> WORK IN PROGRESS</h1>

# 👿 dyablog
*[Django](https://www.djangoproject.com/) + Blog = `dyablog`*

An inconsequential blog built on Django, vaguely following the instructions of a soon to be four year old [YouTube tutorial](https://youtu.be/F5mRW0jo-U4?t=11258).

This project is mainly personal practice fo proper Python project management, making use of pyenv and Poetry following in the footsteps of my earlier, dependency-free, largely version-agnostic [`sudoku-solver`](https://github.com/0xBA5E64/Sudoku-Solver) project.

## Dependencies*
- [`pyenv`](https://github.com/pyenv/pyenv) - Python version manager
  - Python `3.10.7` installed
- [Poetry](https://python-poetry.org/) - Python Package and Dependency manager

\*All remaining project dependencies are managed by Poetry, and are automatically installed through `poetry install`.

## Getting Started
Double-check you fullfill all dependencies, then;
```sh
$ pyenv install 3.10.7 # Install appropriate Python version.
$ git clone https://github.com/0xBA5E64/dyablog # Clone repo
$ cd dyablog # Enter project directory.
$ poetry shell # Open shell in poetry's virtual enviroument.
$ poetry install # Install python project dependencies.
$ code . # Open project in vscode.
```