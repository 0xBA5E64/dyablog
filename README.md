# 👿 dyablog
*[Django](https://www.djangoproject.com/) + Blog = `dyablog`*

An inconsequential personal blog built on Django, based on and maintained and refactored through the years to the best practices of different eras.

> [!NOTE]
> This project is perhaps mostly a personal exercise in proper Python project management, originally as outlined in [Alex Mitelman](https://twitter.com/alex_mitelman)'s article ["Python Best Practices for a New Project in 2021"](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/) through the use of tools such as **`pyenv`** and **Poetry**, since then adapted to astral.sh's wonderful [`uv`](https://docs.astral.sh/uv/). If you do for whatever reason go through the effort to set this up and run it and find yourself a bug, I'd be honored by a report!

## Dependencies
- This project and it's python dependencies are managed through astral.sh's wonderful [`uv`](https://docs.astral.sh/uv/); making Python bearable, nay; *fun* to use since '23
- Aside from that, [TailwindCSS](https://tailwindcss.com/) is used for styling some components of the interface, in an exercise of "modern" web-dev practices, but should be managed automatically through django-tailwind-cli.

## Getting Started
Get uv, then;
```sh
$ git clone https://github.com/0xBA5E64/dyablog # Clone the repository
$ cd dyablog # Enter the project directory
$ uv run ./manage.py collectstatic # Populate project static files
$ uv run ./manage.py migrate # Generate initial empty database
$ uv run ./manage.py createsuperuser # Create an admin account
$ code . # Open project in vscode.
$ uv run ./manage.py tailwind runserver # start the development server *with* Tailwind CSS
```
