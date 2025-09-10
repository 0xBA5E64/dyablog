# 👿 dyablog
*[Django](https://www.djangoproject.com/) + Blog = `dyablog`*

An inconsequential blog built on Django, vaguely following the instructions of ~~a soon-to-be four-year-old [YouTube tutorial](https://youtu.be/F5mRW0jo-U4?t=11258)~~ the official Django 4.1 [introduction/tutorial](https://docs.djangoproject.com/en/4.1/intro/).

> [!NOTE]
> This project is perhaps mostly a personal exercise in proper python project management, originally as outlined in [Alex Mitelman](https://twitter.com/alex_mitelman)'s article ["Python Best Practices for a New Project in 2021"](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/) through the use of tools such as **`pyenv`** and **Poetry**, since then adapted to astral.sh's uv. If you do for whatever reason go through the effort to set this up and run it and find yourself a bug, I'd be honored by a report!

See also the ["wiki"](docs/wiki.md) document for additional project information and instructions.

## Dependencies
- This project and it's python dependencies are managed through astral.sh's wonderful [`uv`](https://docs.astral.sh/uv/); making Python bearable, nay; *fun* to use since '23
- Aside from that, [TailwindCSS](https://tailwindcss.com/) is used for template styles, in an exercise of "modern" web-dev practices. Their [CLI tool](https://tailwindcss.com/docs/installation/tailwind-cli) is required to update and maintain key styles by the project, although should not be strictly neccecary if you are only modifying the backend.

## Getting Started
Get uv, then;
```sh
$ git clone https://github.com/0xBA5E64/dyablog # Clone the repository
$ cd dyablog # Enter the project directory
$ uv run ./manage.py collectstatic # Populate project static files
$ uv run ./manage.py migrate # Generate initial empty database
$ uv run ./manage.py createsuperuser # Create an admin account
$ code . # Open project in vscode.
$ tailwindcss -i blog/static/blog/style.css -o blog/static/blog/tailwind.css -w & uv run ./manage.py runserver # start the development server *with* Tailwind CSS
```
