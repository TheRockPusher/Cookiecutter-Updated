"""Tests for {{cookiecutter.project_name}}."""

import pytest

from {{cookiecutter.project_slug}} import example_function{% if cookiecutter.include_cli %}, main{% endif %}



def test_example_function() -> None:
    """Test example_function."""
    assert example_function("test") == "test"
{% if cookiecutter.include_cli %}


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    """Test main CLI entry point."""
    main()
    captured = capsys.readouterr()
    assert "Hello from {{cookiecutter.project_name}}!" in captured.out
{% endif %}
