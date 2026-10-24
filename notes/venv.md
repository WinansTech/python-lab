# UV Install / Virtual Environment

For this environment we will focus on UV as the package and project manager handler.

- Install once;

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Docker

- uv provides a Docker image at;

```bash
ghcr.io/astral-sh/uv
```

> After installing uv, you can check that uv is available by running the `uv` command in the terminal

## Running The Environment

```bash
# check python version
~/Documents/Dev/Projects/python-lab/exercises$ python3 --version
```

- Create environment;

```bash
uv venv
source .venv/bin/activate 
```

## UV Command list

| Commands  | Descripton                                                 |
| --------- | ---------------------------------------------------------- |
| auth      | Manage authentication                                      |
| run       | Run a command or script                                    |
| init      | Create a new project                                       |
| add       | Add dependencies to the project                            |
| remove    | Remove dependencies from the project                       |
| version   | Read or update the project's version                       |
| sync      | Update the project's environment                           |
| lock      | Update the project's lockfile                              |
| export    | Export the project's lockfile to an alternate format       |
| tree      | Display the project's dependency tree                      |
| format    | Format Python code in the project                          |
| check     | Run checks on the project                                  |
| audit     | Audit the project's dependencies                           |
| tool      | Run and install commands provided by Python packages       |
| python    | Manage Python versions and installations                   |
| pip       | Manage Python packages with a pip-compatible interface     |
| venv      | Create a virtual environment                               |
| build     | Build Python packages into source distributions and wheels |
| publish   | Upload distributions to an index                           |
| workspace | Inspect uv workspaces                                      |
| cache     | Manage uv's cache                                          |
| self      | Manage the uv executable                                   |
| help      | Display documentation for a command                        |

---

## UV Features

### Python versions

Installing and managing Python itself.

- `uv python install`: Install Python versions.
- `uv python list`: View available Python versions.
- `uv python find`: Find an installed Python version.
- `uv python pin`: Pin the current project to use a specific Python version.
- `uv python uninstall`: Uninstall a Python version.

### Scripts

Executing standalone Python scripts, e.g., `example.py`.

- `uv run`: Run a script.
- `uv add --script`: Add a dependency to a script.
- `uv remove --script`: Remove a dependency from a script.

### Projects

Creating and working on Python projects, i.e., with a `pyproject.toml`.

- `uv init`: Create a new Python project.
- `uv add`: Add a dependency to the project.
- `uv remove`: Remove a dependency from the project.
- `uv sync`: Sync the project's dependencies with the environment.
- `uv lock`: Create a lockfile for the project's dependencies.
- `uv run`: Run a command in the project environment.
- `uv tree`: View the dependency tree for the project.
- `uv build`: Build the project into distribution archives.
- `uv publish`: Publish the project to a package index.

### Tools

Running and installing tools published to Python package indexes, e.g., `ruff` or `black`.

- `uvx` / `uv tool run`: Run a tool in a temporary environment.
- `uv tool install`: Install a tool user-wide.
- `uv tool uninstall`: Uninstall a tool.
- `uv tool list`: List installed tools.
- `uv tool update-shell`: Update the shell to include tool executables.

### Utility

Managing and inspecting uv's state, such as the cache, storage directories, or performing a self-update:

- `uv cache clean`: Remove cache entries.
- `uv cache prune`: Remove outdated cache entries and all centralized project environments.
- `uv cache dir`: Show the uv cache directory path.
- `uv tool dir`: Show the uv tool directory path.
- `uv python dir`: Show the uv installed Python versions path.
- `uv self update`: Update uv to the latest version.

---
