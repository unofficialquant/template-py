# Template

GitHub Python repository template.

## Folder Structure

- `.github` contains GitHub related configurations.
- `assets` contains assets used by the project.
- `docs` contains documentation.
- `scripts` contains scripts used by the project.
- `src` contains source code.
- `tests` contains tests.
- `tools` contains tools used by the project.

## Setup

```bash
# Install core dependencies
pip install -r requirements.txt

# Install dev dependencies for development
pip install -r requirements-dev.txt

# Pre-commit
pre-commit install --hook-type commit-msg
```
