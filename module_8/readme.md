*This project has been created as part of the 42 curriculum by mfakih.*


# Python Data Engineering Guide
A comprehensive guide to virtual environments, package management, and secure configuration
---

## Table of Contents
1. Virtual Environments (venvs)

2. System Path and Package Detection

3. Curl and Package Managers
 
4. Poetry: Python Dependency Management
 
5. Import Checking and Version Detection
 
6. Matplotlib Basics
 
7. Environment Variables and .env Files


## Virtual Environments (venvs)
### What are they?
Virtual environments are isolated Python environments that allow you to manage dependencies for different projects separately. Each project gets its own "room" with its own packages.

###Why use them?
Different projects need different package versions

Avoid conflicts between packages

No need for admin/sudo permissions

Reproducible environments

### How to create one
python3 -m venv environment_name

Common naming: venv, .venv, project_env, matrix_env

How to activate
Linux/Mac:

source environment_name/bin/activate

. environment_name/bin/activate (shorter syntax)

Windows:

Command Prompt: environment_name\Scripts\activate.bat

PowerShell: environment_name\Scripts\Activate.ps1

How to deactivate
deactivate

Check if you're in one
which python — should show path to your venv, not /usr/bin/python

System Path and Package Detection
Detecting virtual environment
Compare sys.prefix vs sys.base_prefix — if they're different, you're in a venv.

Getting environment name
os.path.basename(sys.prefix) gives you just the folder name.

Finding package locations
site.getsitepackages() shows where packages are installed.

## Curl and Package Managers
What is Curl?
Curl (Client URL) is a command-line tool for downloading files and interacting with APIs. Think of it as a browser for your terminal.
---
Install Curl on Linux
text
sudo apt update
sudo apt install curl
curl --version
The Three Package Managers
Manager	What it manages	Where from
apt	System packages	Ubuntu/Debian repos
pip	Python packages	PyPI (Python Package Index)
curl	Any file/URL	Any web server
What each does
apt: Installs system-level software (like Python itself)

pip: Installs Python libraries (like pandas, requests)

curl: Downloads anything from anywhere

Why we use curl to install Poetry
Poetry provides an installation script online. Curl downloads it, then we pipe it to Python to run it.

Poetry: Python Dependency Management
What is Poetry?
Poetry is a dependency management and packaging tool for Python. It's like pip on steroids — it manages virtual environments, dependencies, and project metadata automatically.

Install Poetry
text
curl -sSL https://install.python-poetry.org | python3 -
Add to PATH if needed:

text
export PATH="$HOME/.local/bin:$PATH"
Poetry commands
poetry new project-name — Create new project

poetry init — Initialize in existing directory (interactive)

poetry add package-name — Add a dependency

poetry add --dev package-name — Add dev dependency

poetry install — Install all dependencies

poetry install --no-root — Install deps but not the project itself

poetry update — Update dependencies

poetry show — List installed packages

poetry run command — Run command in venv

poetry shell — Activate the virtual environment

poetry env info --path — Show where venv is located

What is pyproject.toml?
TOML = Tom's Obvious, Minimal Language. It's a configuration file format that's easy for humans to read and machines to parse. It contains all your project metadata and dependencies.

What is poetry.lock?
Locks exact versions of every dependency. Ensures everyone working on the project gets exactly the same versions. Never edit it manually.

The --no-root flag
Tells Poetry: "Install all dependencies, but don't install the current project as a package." Useful in CI/CD pipelines.

Import Checking and Version Detection
Best way to check if a package exists
Try to import it. If it fails with ImportError, it's not installed.

Getting package version
Most packages store version in __version__ attribute.

What happens when import fails
Python raises an ImportError — catch it with try-except to handle gracefully.

Matplotlib Basics
Common functions
plt.figure() — Create a new figure/canvas

plt.hist() — Create histogram

plt.title() — Add title

plt.xlabel() / plt.ylabel() — Add axis labels

plt.legend() — Add legend

plt.grid() — Add grid lines

plt.savefig('filename.png') — Save as PNG

plt.close() — Close figure (free memory)

Environment Variables and .env Files
What is a .env file?
A simple text file that stores configuration and secrets separate from your code.

Why use it?
Never hardcode sensitive information:

❌ Database URLs with passwords

❌ API keys

❌ Secret tokens

The two-file pattern
.env — Contains real values. Never commit to git.

.env.example — Contains placeholder values. Safe to commit.

.gitignore must include
Always add .env to .gitignore to prevent accidentally committing secrets.

Reading environment variables
os.getenv('VARIABLE_NAME') — Returns None if not found, never crashes.

os.getenv('VARIABLE_NAME', 'default_value') — Provides fallback.

Priority order
Real environment variables (set in terminal)

Variables from .env file

Default values in code

Remember: In the real world of data engineering, these tools keep your systems secure, maintainable, and scalable.