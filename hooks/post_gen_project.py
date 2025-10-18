"""Post-generation hook for cookiecutter template cleanup and initialization."""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def remove_file_or_dir(path: str) -> None:
    """Remove a file or directory if it exists."""
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            print(f"  Removed: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"  Removed directory: {path}")


def cleanup_conditional_files() -> None:
    """Remove files based on user choices."""
    print("\n" + "=" * 60)
    print("Cleaning up conditional files...")
    print("=" * 60)

    use_codecov = {{ "True" if cookiecutter.use_codecov else "False" }}

    # Codecov configuration (optional)
    if not use_codecov:
        print("\n📦 Codecov disabled - no additional cleanup needed")
        print("  (Codecov integration is conditional in CI workflow)")
    else:
        print("\n📦 Codecov enabled - integration configured in CI workflow")

    print("\n✓ Conditional cleanup complete")


def initialize_git() -> None:
    """Initialize git repository."""
    print("\n" + "=" * 60)
    print("Initializing git repository...")
    print("=" * 60)

    try:
        # Check if git is installed
        subprocess.run(
            ["git", "--version"],
            check=True,
            capture_output=True,
            text=True,
        )

        # Initialize git repo with main branch
        subprocess.run(
            ["git", "init", "-b", "main"],
            check=True,
            capture_output=True,
            text=True,
        )
        print("✓ Git repository initialized with 'main' branch")

        # Create initial commit
        subprocess.run(
            ["git", "add", "."],
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit from cookiecutter template"],
            check=True,
            capture_output=True,
            text=True,
        )
        print("✓ Initial commit created")

    except subprocess.CalledProcessError as e:
        print(f"⚠ Warning: Git initialization failed: {e}")
        print("  You can initialize git manually later with: git init -b main")
    except FileNotFoundError:
        print("⚠ Warning: Git not found in PATH")
        print("  Install git and run: git init -b main")


def install_dependencies() -> None:
    """Install dependencies using uv."""
    print("\n" + "=" * 60)
    print("Installing dependencies with UV...")
    print("=" * 60)

    try:
        # Check if uv is installed
        subprocess.run(
            ["uv", "--version"],
            check=True,
            capture_output=True,
            text=True,
        )

        # Run uv sync to install dependencies
        print("\n📦 Running 'uv sync'...")
        result = subprocess.run(
            ["uv", "sync"],
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)
        print("✓ Dependencies installed successfully")

        # Install pre-commit hooks
        print("\n🔧 Installing pre-commit hooks...")
        result = subprocess.run(
            ["uv", "run", "pre-commit", "install"],
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)
        print("✓ Pre-commit hooks installed")

    except subprocess.CalledProcessError as e:
        print(f"\n⚠ Warning: UV installation failed: {e}")
        print("  Run 'make install' manually after project creation")
    except FileNotFoundError:
        print("\n⚠ Warning: UV not found in PATH")
        print("  Install UV from: https://github.com/astral-sh/uv")
        print("  Then run: make install")


def print_next_steps() -> None:
    """Print next steps for the user."""
    project_name = "{{ cookiecutter.project_name }}"
    project_slug_hyphenated = "{{ cookiecutter.project_slug_hyphenated }}"
    github_username = "{{ cookiecutter.github_username }}"

    print("\n" + "=" * 60)
    print(f"🎉 {project_name} created successfully!")
    print("=" * 60)

    print("\n📁 Project created at:")
    print(f"   {os.getcwd()}")

    print("\n🚀 Next steps:")
    print(f"\n  1. Review and customize your project:")
    print(f"     cd {project_slug_hyphenated}")
    print(f"     cat README.md")

    print(f"\n  2. Run tests and quality checks:")
    print(f"     make check    # Format, lint, type-check")
    print(f"     make test     # Run tests")

    print(f"\n  3. Set up your GitHub repository:")
    print(f"     # Create repository at: https://github.com/{github_username}/{project_slug_hyphenated}")
    print(f"     git remote add origin git@github.com:{github_username}/{project_slug_hyphenated}.git")
    print(f"     git push -u origin main")

    use_codecov = {{ "True" if cookiecutter.use_codecov else "False" }}
    if use_codecov:
        print(f"\n  4. Set up Codecov:")
        print(f"     # Go to: https://codecov.io/gh/{github_username}/{project_slug_hyphenated}")
        print(f"     # Add CODECOV_TOKEN to GitHub repository secrets")

    print(f"\n  5. Start developing:")
    print(f"     # Edit src/{{ cookiecutter.project_slug }}/__init__.py")
    print(f"     # Add tests in tests/")
    print(f"     make format   # Auto-format your code")

    print("\n📖 Documentation:")
    print(f"   README.md           - Project overview and usage")
    print(f"   CONTRIBUTING.md     - Contribution guidelines")
    print(f"   Makefile            - Run 'make help' for all commands")

    print("\n" + "=" * 60)
    print("Happy coding! 🐍")
    print("=" * 60 + "\n")


def main() -> None:
    """Run post-generation tasks."""
    try:
        cleanup_conditional_files()
        initialize_git()
        install_dependencies()
        print_next_steps()

    except Exception as e:
        print(f"\n❌ Error during post-generation: {e}")
        print("The project was created but some setup steps failed.")
        print("You may need to complete setup manually.")
        sys.exit(1)


if __name__ == "__main__":
    main()
