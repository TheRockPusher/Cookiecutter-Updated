# {{cookiecutter.project_name}}

{{cookiecutter.description}}

[![CI](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-{{cookiecutter.python_version}}+-blue.svg)](https://www.python.org/downloads/)
[![License: {{cookiecutter.license}}](https://img.shields.io/badge/License-{{cookiecutter.license}}-blue.svg)](LICENSE)
{% if cookiecutter.use_codecov -%}
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}})
{% endif -%}

## Features

- Modern Python packaging with [UV](https://github.com/astral-sh/uv)
- `src/` layout for better project structure
- Comprehensive code quality tools:
  - [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
  - [Ty](https://github.com/python/ty) for static type checking
  - [pytest](https://pytest.org/) with coverage reporting
- Pre-commit hooks for automated code quality checks
- GitHub Actions CI/CD workflows
- Automated releases with version bumping
{% if cookiecutter.use_codecov -%}
- Code coverage reporting with Codecov
{% endif %}

## Installation

### Prerequisites

- Python {{cookiecutter.python_version}} or higher
- [UV](https://github.com/astral-sh/uv) package manager

Install UV:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install the package

```bash
# Install from PyPI (when published)
uv pip install {{cookiecutter.project_slug_hyphenated}}

# Install from source
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}.git
cd {{cookiecutter.project_slug_hyphenated}}
uv sync
```

## Usage

```python
from {{cookiecutter.project_slug}} import example_function

result = example_function("test")
print(result)  # Output: test
```
{% if cookiecutter.include_cli %}

### Command Line Interface

```bash
{{cookiecutter.project_slug_hyphenated}}
# Output: Hello from {{cookiecutter.project_name}}!
```
{% endif %}

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}.git
cd {{cookiecutter.project_slug_hyphenated}}

# Install dependencies and pre-commit hooks
make install
```

### Available Make Commands

Run `make help` to see all available commands:

```bash
make install         # Install the virtual environment and pre-commit hooks
make format          # Format code with ruff
make format-check    # Check code formatting
make lint-check      # Lint code with ruff
make type-check      # Run static type checking with ty
make check           # Run all code quality checks
make test            # Run tests with pytest
```

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
make test FILE=tests/test_main.py

# Run with coverage report
uv run pytest --cov={{cookiecutter.project_slug}} --cov-report=html
```

### Code Quality

This project maintains high code quality standards:

- **Formatting**: Automated with Ruff (120 character line length)
- **Linting**: Comprehensive rules including security checks (Bandit)
- **Type Checking**: Enforced with Ty
- **Testing**: Minimum 80% code coverage required
- **Documentation**: Google-style docstrings

All checks run automatically via pre-commit hooks and CI/CD.

## Project Structure

```
{{cookiecutter.project_slug_hyphenated}}/
├── src/
│   └── {{cookiecutter.project_slug}}/     # Main package code
│       ├── __init__.py
│       └── py.typed                      # PEP 561 type marker
├── tests/                                 # Test suite
│   └── test_main.py
├── .github/
│   ├── actions/
│   │   └── setup-python-env/             # Reusable setup action
│   └── workflows/
│       ├── ci.yml                        # CI pipeline
│       └── release.yml                   # Release automation
├── pyproject.toml                        # Project configuration
├── Makefile                              # Development commands
├── .pre-commit-config.yaml               # Pre-commit hooks
└── README.md                             # This file
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks (`make check && make test`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Releasing

This project uses automated releases via GitHub Actions:

1. Go to Actions → Release workflow
2. Click "Run workflow"
3. Select version bump type (patch/minor/major)
4. Optionally select pre-release type (alpha/beta/rc)
5. The workflow will:
   - Run all tests
   - Bump the version
   - Update the lockfile
   - Create a git tag
   - Build the package
   - Create a GitHub release

## License

This project is licensed under the {{cookiecutter.license}} License - see the [LICENSE](LICENSE) file for details.

## Author

**{{cookiecutter.author_name}}** - [{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}})

## Acknowledgments

- Built with [UV](https://github.com/astral-sh/uv) - Fast Python package manager
- Linting and formatting by [Ruff](https://github.com/astral-sh/ruff)
- Type checking with [Ty](https://github.com/python/ty)
- Testing with [pytest](https://pytest.org/)

## Links

- **Repository**: [https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}})
- **Issues**: [https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}/issues](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug_hyphenated}}/issues)
