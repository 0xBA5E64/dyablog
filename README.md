<h1 style="color: white; font-weight: normal; text-align: center; background: repeating-linear-gradient(45deg, #F22 0%, #F22 5%, #822 5%, #822 10%); margin: 32px 0; padding: 8px 0; text-shadow: #0004 0px 2px; border-radius: 4px; border: solid 1px #422;" ><b>HEAVILY</b> WORK IN PROGRESS</h1>

# 👿 dyablog
*[Django](https://www.djangoproject.com/) + Blog = `dyablog`*

An inconsequential blog built on Django, vaguely following the instructions of ~~a soon-to-be four-year-old [YouTube tutorial](https://youtu.be/F5mRW0jo-U4?t=11258)~~ the official Django 4.1 [introduction/tutorial](https://docs.djangoproject.com/en/4.1/intro/).

This project is mainly a personal exercise in proper python project management as outlined in [Alex Mitelman](https://twitter.com/alex_mitelman)'s article ["Python Best Practices for a New Project in 2021"](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/) through the use of tools such as **`pyenv`** and **Poetry**.
*(this is in contrast to my earlier dependency-free, largely version-agnostic [`sudoku-solver`](https://github.com/0xBA5E64/Sudoku-Solver) project)*

See the ["wiki"](docs/wiki.md) document for additional project information and instructions.

## Dependencies*
- [`pyenv`](https://github.com/pyenv/pyenv) - Python version manager
  - Python `3.10.7` installed
- [Poetry](https://python-poetry.org/) - Python Package and Dependency manager
- [TailwindCSS](https://tailwindcss.com/docs/installation) [CLI](https://tailwindcss.com/docs/installation) tool.
  - Available through npm: `npm install -D tailwindcss`
  - or [Standalone](https://tailwindcss.com/blog/standalone-cli)

\*All remaining project dependencies are managed by Poetry, and are automatically installed through `poetry install`.

## Getting Started
Double-check you fulfill all dependencies, then;
```sh
$ pyenv install 3.10.7 # Install appropriate Python version.
$ git clone https://github.com/0xBA5E64/dyablog # Clone repo
$ cd dyablog # Enter project directory.
$ poetry shell # Open shell in poetry's virtual enviroument.
$ poetry install # Install python project dependencies.
$ python ./manage.py collectstatic # populate project static files
$ tailwind -i ./blog/static/blog/style.css -o ./blog/static/blog/tailwind.css -w & ./manage.py runserver # start the development server *with* Tailwind CSS
$ code . # Open project in vscode.
```
