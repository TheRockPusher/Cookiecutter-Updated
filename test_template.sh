#!/bin/bash
# Test script for cookiecutter template

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COOKIECUTTER_CONFIG="$SCRIPT_DIR/cookiecutter.json"

DEFAULT_PROJECT_NAME=$(COOKIECUTTER_CONFIG_PATH="$COOKIECUTTER_CONFIG" python3 - <<'PY'
import json
import os
from pathlib import Path

config_path = Path(os.environ["COOKIECUTTER_CONFIG_PATH"])
with config_path.open(encoding="utf-8") as handle:
    data = json.load(handle)

print(data["project_name"])
PY
)

DEFAULT_PROJECT_DESCRIPTION=$(COOKIECUTTER_CONFIG_PATH="$COOKIECUTTER_CONFIG" python3 - <<'PY'
import json
import os
from pathlib import Path

config_path = Path(os.environ["COOKIECUTTER_CONFIG_PATH"])
with config_path.open(encoding="utf-8") as handle:
    data = json.load(handle)

print(data["description"])
PY
)

echo "🧪 Testing Cookiecutter Template"
echo "================================="

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test directory
TEST_DIR="test-cookiecutter-output"

# Cleanup
echo "🧹 Cleaning up old test projects..."
rm -rf "$TEST_DIR"
mkdir -p "$TEST_DIR"

# Test 1: Default values
echo ""
echo "📦 Test 1: Generating project with default values..."
cd "$TEST_DIR"
uvx --with jinja2-time cookiecutter .. --no-input

PROJECT_DIR=$(find . -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | head -n 1)

if [ -n "$PROJECT_DIR" ] && [ -d "$PROJECT_DIR" ]; then
    echo -e "${GREEN}✅ Test 1 PASSED: Project '$PROJECT_DIR' created${NC}"
else
    echo -e "${RED}❌ Test 1 FAILED: Project not created${NC}"
    exit 1
fi

cd "$PROJECT_DIR"

PACKAGE_DIR=$(find src -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | head -n 1)

if [ -z "$PACKAGE_DIR" ]; then
    echo -e "${RED}❌ Test 1 FAILED: Could not determine package directory${NC}"
    exit 1
fi

# Test 2: Check critical files exist
echo ""
echo "📋 Test 2: Checking critical files exist..."
REQUIRED_FILES=(
    "pyproject.toml"
    "README.md"
    "LICENSE"
    "Makefile"
    ".gitignore"
    ".pre-commit-config.yaml"
    ".python-version"
    "src/$PACKAGE_DIR/__init__.py"
    "src/$PACKAGE_DIR/py.typed"
    "tests/test_main.py"
    ".github/workflows/ci.yml"
    ".github/workflows/release.yml"
    ".github/actions/setup-python-env/action.yml"
)

MISSING_FILES=0
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ] && [ ! -d "$file" ]; then
        echo -e "${RED}❌ Missing: $file${NC}"
        MISSING_FILES=$((MISSING_FILES + 1))
    fi
done

if [ $MISSING_FILES -eq 0 ]; then
    echo -e "${GREEN}✅ Test 2 PASSED: All required files exist${NC}"
else
    echo -e "${RED}❌ Test 2 FAILED: $MISSING_FILES files missing${NC}"
    exit 1
fi

# Ensure optional Claude assets are absent when not selected
if [ -e "CLAUDE.md" ] || [ -d ".claude" ]; then
    echo -e "${RED}❌ Test 2 FAILED: Claude AI assets should not exist by default${NC}"
    exit 1
fi

# Test 3: Verify variable substitution
echo ""
echo "🔍 Test 3: Verifying variable substitution..."
if grep -q "name = \"$PROJECT_DIR\"" pyproject.toml && \
   grep -q "description = \"$DEFAULT_PROJECT_DESCRIPTION\"" pyproject.toml && \
   grep -q "def example_function" "src/$PACKAGE_DIR/__init__.py"; then
    echo -e "${GREEN}✅ Test 3 PASSED: Variables correctly substituted${NC}"
else
    echo -e "${RED}❌ Test 3 FAILED: Variable substitution issues${NC}"
    exit 1
fi

# Test 4: Check no template syntax remains
echo ""
echo "🔍 Test 4: Checking for remaining template syntax..."
if grep -r "{{cookiecutter" . 2>/dev/null | grep -v ".git" | grep -v "node_modules"; then
    echo -e "${RED}❌ Test 4 FAILED: Found unreplaced template variables${NC}"
    exit 1
else
    echo -e "${GREEN}✅ Test 4 PASSED: No template syntax remaining${NC}"
fi

# Test 5: Verify pyproject.toml is valid TOML
echo ""
echo "📝 Test 5: Validating pyproject.toml..."
if uv run python -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))" 2>/dev/null; then
    echo -e "${GREEN}✅ Test 5 PASSED: pyproject.toml is valid TOML${NC}"
else
    echo -e "${RED}❌ Test 5 FAILED: pyproject.toml is invalid${NC}"
    exit 1
fi

# Test 6: Run quality checks
echo ""
echo "🔧 Test 6: Running code quality checks..."
if make check; then
    echo -e "${GREEN}✅ Test 6 PASSED: Quality checks passed${NC}"
else
    echo -e "${RED}❌ Test 6 FAILED: Quality checks failed${NC}"
    exit 1
fi

# Test 7: Run tests
echo ""
echo "🧪 Test 7: Running tests..."
if make test; then
    echo -e "${GREEN}✅ Test 7 PASSED: Tests passed${NC}"
else
    echo -e "${RED}❌ Test 7 FAILED: Tests failed${NC}"
    exit 1
fi

# Test 8: Verify imports work
echo ""
echo "📦 Test 8: Testing imports..."
if uv run python -c "from $PACKAGE_DIR import example_function; assert example_function('test') == 'test'"; then
    echo -e "${GREEN}✅ Test 8 PASSED: Imports work correctly${NC}"
else
    echo -e "${RED}❌ Test 8 FAILED: Import errors${NC}"
    exit 1
fi

# Test 9: Verify CLI works
echo ""
echo "🖥️  Test 9: Testing CLI entry point..."
CLI_COMMAND="$PROJECT_DIR"
OUTPUT=$(uv run "$CLI_COMMAND")
if echo "$OUTPUT" | grep -q "Hello from $DEFAULT_PROJECT_NAME"; then
    echo -e "${GREEN}✅ Test 9 PASSED: CLI works correctly${NC}"
else
    echo -e "${RED}❌ Test 9 FAILED: CLI output incorrect${NC}"
    exit 1
fi

# Test 10: Check git initialization
echo ""
echo "📚 Test 10: Checking git initialization..."
if [ -d ".git" ] && git log --oneline | grep -q "Initial commit"; then
    echo -e "${GREEN}✅ Test 10 PASSED: Git repository initialized${NC}"
else
    echo -e "${RED}❌ Test 10 FAILED: Git not initialized properly${NC}"
    exit 1
fi

# Summary
echo ""
echo "================================="
echo -e "${GREEN}🎉 ALL TESTS PASSED!${NC}"
echo "================================="
echo ""
echo "Generated project location:"
echo "  $(pwd)"
echo ""
echo "Next steps:"
echo "  1. Review the generated files"
echo "  2. Customize as needed"
echo "  3. Push to GitHub"
echo ""
