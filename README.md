# Cookiecutter Python UV Template

A modern, production-ready cookiecutter template for Python projects using UV, featuring comprehensive tooling, CI/CD, and best practices for 2025.

## Features

This template generates a Python project with:

### 🚀 Modern Tooling
- **[UV](https://github.com/astral-sh/uv)** - Lightning-fast Python package manager (10-100× faster than pip)
- **[Ruff](https://github.com/astral-sh/ruff)** - Unified linter and formatter (replaces flake8, black, isort, and more)
- **[Ty](https://github.com/python/ty)** - Modern static type checker
- **[pytest](https://pytest.org/)** - Comprehensive testing framework with coverage

### 📦 Best Practices
- **src/ layout** - Proper package structure for better testability
- **pyproject.toml** - Modern Python packaging (PEP 621)
- **Type hints** - Full type safety with `py.typed` marker (PEP 561)
- **Pre-commit hooks** - Automatic code quality checks
- **80%+ coverage** - Enforced test coverage threshold

### 🔧 Development Workflow
- **Makefile** - Simple commands for common tasks
- **Pre-commit** - Automated formatting and linting
- **Comprehensive linting** - Security (Bandit), complexity, best practices
- **Google-style docstrings** - Clear documentation standards

### 🤖 CI/CD Automation
- **GitHub Actions** - Automated testing and quality checks
- **Matrix testing** - Test across Python versions
- **Automated releases** - Version bumping and GitHub releases
- **Optional Codecov** - Code coverage reporting

### 🐳 Optional Features
- **Codecov integration** - Code coverage reporting and tracking
- **CLI entry point** - Command-line interface scaffolding

## Prerequisites

- **Python 3.9+** (3.13 recommended)
- **UV** - Install from [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
- **Git** - For version control

Install UV:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Quick Start

### Using UVX (Recommended)

```bash
# From the template directory
uvx --with jinja2-time cookiecutter .

# Or if you want to use a specific path
uvx --with jinja2-time cookiecutter /path/to/Cookiecutter-Updated
```

### Using Cookiecutter Directly

```bash
# Install cookiecutter
uv tool install cookiecutter

# Generate project (you'll need jinja2-time)
pip install jinja2-time
cookiecutter .
```

## Template Options

You'll be prompted for the following options:

| Option | Description | Example |
|--------|-------------|---------|
| `project_name` | Full project name | `My Awesome Project` |
| `project_slug` | Python package name (auto-generated) | `my_awesome_project` |
| `project_slug_hyphenated` | Repository name (auto-generated) | `my-awesome-project` |
| `description` | Short project description | `A Python project with modern tooling` |
| `author_name` | Your full name | `Jane Doe` |
| `author_email` | Your email address | `jane@example.com` |
| `github_username` | GitHub username or org | `janedoe` |
| `python_version` | Minimum Python version | `3.13` |
| `license` | Project license | `MIT`, `Apache-2.0`, `BSD-3-Clause`, `GPL-3.0`, `Proprietary` |
| `use_codecov` | Enable Codecov integration | `false` / `true` |
| `include_cli` | Include CLI entry point | `true` / `false` |

## Generated Project Structure

```
my-awesome-project/
├── .github/
│   ├── actions/
│   │   └── setup-python-env/action.yml  # Reusable GitHub Action
│   └── workflows/
│       ├── ci.yml                        # CI pipeline
│       └── release.yml                   # Release automation
├── src/
│   └── my_awesome_project/
│       ├── __init__.py                   # Main module
│       └── py.typed                      # PEP 561 type marker
├── tests/
│   └── test_main.py                      # Test suite
├── .gitignore                            # Comprehensive ignore patterns
├── .pre-commit-config.yaml               # Pre-commit hooks
├── .python-version                       # Python version file
├── CONTRIBUTING.md                       # Contribution guidelines
├── LICENSE                               # Chosen license
├── Makefile                              # Development commands
├── pyproject.toml                        # Project configuration
└── README.md                             # Project documentation
```

## After Generation

The template automatically:

1. ✅ Validates all inputs
2. ✅ Generates project from template
3. ✅ Initializes git repository
4. ✅ Installs dependencies with UV
5. ✅ Sets up pre-commit hooks
6. ✅ Creates initial commit

### Next Steps

```bash
cd my-awesome-project

# Run tests and quality checks
make check    # Format, lint, type-check
make test     # Run tests

# Set up GitHub repository
git remote add origin git@github.com:USERNAME/my-awesome-project.git
git push -u origin main

# Start developing
# Edit src/my_awesome_project/__init__.py
# Add tests in tests/
make format   # Auto-format code
```

## Development Commands

Run `make help` in the generated project to see all available commands:

```bash
make install         # Install virtual environment
make format          # Format code with ruff
make format-check    # Check code formatting
make lint-check      # Lint code
make type-check      # Run type checking
make check           # Run all quality checks
make test            # Run tests with coverage
```

## CI/CD Workflows

### Continuous Integration

Runs automatically on push and pull requests:
- ✅ Code formatting checks (Ruff)
- ✅ Linting (Ruff with comprehensive rules)
- ✅ Type checking (Ty)
- ✅ Unit tests (pytest)
- ✅ Code coverage (80% minimum)
- ✅ Optional Codecov reporting

### Automated Releases

Manual workflow dispatch for version bumping:
1. Go to Actions → Release
2. Select bump type (patch/minor/major)
3. Optionally select pre-release type (alpha/beta/rc)
4. Workflow automatically:
   - Runs full test suite
   - Bumps version in pyproject.toml
   - Updates uv.lock
   - Creates git tag
   - Builds package
   - Creates GitHub release

## Code Quality Standards

Generated projects enforce:

- **Line length**: 120 characters
- **Type hints**: Required on all functions
- **Docstrings**: Google-style, required
- **Test coverage**: Minimum 80%
- **Security**: Bandit security linting
- **Best practices**: Pylint, bugbear, simplify, and more

## Testing the Template

To test that the template works correctly:

```bash
# Generate a test project with default values
uvx --with jinja2-time cookiecutter . --no-input

# Or with custom values
uvx --with jinja2-time cookiecutter . \
  project_name="Test Project" \
  author_name="Test Author" \
  author_email="test@example.com" \
  github_username="testuser"

# Run the automated test script
./test_template.sh
```

## Troubleshooting

### UV Not Found

Install UV first:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### "No module named 'jinja2_time'" Error

Use the `--with jinja2-time` flag with uvx:
```bash
uvx --with jinja2-time cookiecutter .
```

This ensures the required Jinja2 extension is available during template generation.

### Pre-commit Hooks Fail

Update and run manually:
```bash
uv run pre-commit autoupdate
uv run pre-commit run --all-files
```

### Template Generation Fails

Check that you have:
- Python 3.9+
- Git installed
- Valid email format
- Valid Python package name (no hyphens in project_slug)
- Using `--with jinja2-time` flag with uvx

## License

This template is licensed under the MIT License. Generated projects use the license you select during generation.

## Credits

Built with:
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) - Template engine
- [UV](https://github.com/astral-sh/uv) - Fast Python package manager
- [Ruff](https://github.com/astral-sh/ruff) - Lightning-fast linter/formatter
- [Ty](https://github.com/python/ty) - Type checker
- [pytest](https://pytest.org/) - Testing framework

Based on best practices from:
- [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv)
- Modern Python packaging standards (PEP 517, 518, 621, 561)

---

**Happy coding with modern Python tooling! 🐍✨**
