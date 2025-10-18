"""Pre-generation hook for cookiecutter template validation."""

import re
import sys


def validate_project_slug() -> None:
    """Validate that project_slug is a valid Python identifier."""
    project_slug = "{{ cookiecutter.project_slug }}"

    # Python identifier regex
    python_identifier_regex = r"^[_a-zA-Z][_a-zA-Z0-9]*$"

    if not re.match(python_identifier_regex, project_slug):
        print(f"ERROR: '{project_slug}' is not a valid Python module name!")
        print("Module names must:")
        print("  - Start with a letter or underscore")
        print("  - Contain only letters, numbers, and underscores")
        print("  - Not use hyphens or spaces")
        sys.exit(1)

    print(f"✓ Project slug '{project_slug}' is valid")


def validate_email() -> None:
    """Validate that author_email has a basic email format."""
    author_email = "{{ cookiecutter.author_email }}"

    # Basic email regex
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not re.match(email_regex, author_email):
        print(f"ERROR: '{author_email}' is not a valid email address!")
        sys.exit(1)

    print(f"✓ Email '{author_email}' is valid")


def validate_python_version() -> None:
    """Validate that python_version is in a valid format."""
    python_version = "{{ cookiecutter.python_version }}"

    # Version regex (e.g., 3.9, 3.10, 3.11, etc.)
    version_regex = r"^3\.\d{1,2}$"

    if not re.match(version_regex, python_version):
        print(f"ERROR: '{python_version}' is not a valid Python version!")
        print("Version must be in format: 3.X (e.g., 3.9, 3.10, 3.11)")
        sys.exit(1)

    # Check if version is supported (3.9+)
    major, minor = map(int, python_version.split('.'))
    if major != 3 or minor < 9:
        print(f"ERROR: Python {python_version} is not supported!")
        print("Minimum supported version is Python 3.9")
        sys.exit(1)

    print(f"✓ Python version '{python_version}' is valid")


def main() -> None:
    """Run all validations."""
    print("=" * 60)
    print("Validating cookiecutter template inputs...")
    print("=" * 60)

    try:
        validate_project_slug()
        validate_email()
        validate_python_version()

        print("=" * 60)
        print("✓ All validations passed!")
        print("=" * 60)

    except Exception as e:
        print(f"\nUnexpected error during validation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
