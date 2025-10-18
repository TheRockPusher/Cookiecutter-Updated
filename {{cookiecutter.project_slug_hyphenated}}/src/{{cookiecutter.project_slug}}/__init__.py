"""{{cookiecutter.description}}."""

__version__ = "0.1.0"


def example_function(value: str) -> str:
    """Return the input value unchanged.

    Args:
        value: The input string to return.

    Returns:
        The same string that was passed in.

    """
    return value

{% if cookiecutter.include_cli %}

def main() -> None:
    """CLI entry point."""
    print("Hello from {{cookiecutter.project_name}}!")
{% endif %}
