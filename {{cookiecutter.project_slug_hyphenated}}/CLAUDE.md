# CLAUDE.md

This file provides comprehensive guidance to Claude Code when working with Python code in this repository.

## Core Development Philosophy

### KISS (Keep It Simple, Stupid)

Simplicity should be a key goal in design. Choose straightforward solutions over complex ones whenever possible. Simple solutions are easier to understand, maintain, and debug.

### YAGNI (You Aren't Gonna Need It)

Avoid building functionality on speculation. Implement features only when they are needed, not when you anticipate they might be useful in the future.

### Design Principles

- **Dependency Inversion**: High-level modules should not depend on low-level modules. Both should depend on abstractions.
- **Open/Closed Principle**: Software entities should be open for extension but closed for modification.
- **Single Responsibility**: Each function, class, and module should have one clear purpose.
- **Fail Fast**: Check for potential errors early and raise exceptions immediately when issues occur.
- **Pythonic Patterns**: Embrace Python's data model through special methods, protocols, and built-in idioms.
- **No heavy inheritance**: Prefer composition and Protocols over nested inheritance hierarchies.

## 🧱 Code Structure & Modularity

### File and Function Limits

- **Never create a file longer than 500 lines of code**. If approaching this limit, refactor by splitting into modules.
- **Functions should be under 50 lines** with a single, clear responsibility.
- **Classes should be under 100 lines** and represent a single concept or entity.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.

### Project Architecture

Follow strict vertical slice architecture with tests living next to the code they test:

```bash
project/
    __init__.py
    main.py
    tests/
        test_main.py
    conftest.py

    # Core modules
    database/
        __init__.py
        connection.py
        models.py
        tests/
            test_connection.py
            test_models.py

    auth/
        __init__.py
        authentication.py
        authorization.py
        tests/
            test_authentication.py
            test_authorization.py

    # Feature slices
    features/
        user_management/
            __init__.py
            handlers.py
            validators.py
            tests/
                test_handlers.py
                test_validators.py

        payment_processing/
            __init__.py
            processor.py
            gateway.py
            tests/
                test_processor.py
                test_gateway.py
```

## 🛠️ Development Environment

### UV Package Management

This project uses UV for blazing-fast Python package and environment management.

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Sync dependencies
uv sync

# Add a package ***NEVER UPDATE A DEPENDENCY DIRECTLY IN PYPROJECT.toml***
# ALWAYS USE UV ADD
uv add requests

# Add development dependency
uv add --dev pytest ruff mypy

# Remove a package
uv remove requests

# Run commands in the environment
uv run python script.py
uv run pytest
uv run ruff check .

# Install specific Python version
uv python install 3.12
```

### Development Commands

```bash
# Run all tests
uv run pytest

# Run specific tests with verbose output
uv run pytest tests/test_module.py -v

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Fix linting issues automatically
uv run ruff check --fix .
```

## 📋 Style & Conventions

### Python Style Guide

- **Follow PEP8** with these specific choices:
  - Line length: 100 characters (set by Ruff in pyproject.toml)
  - Use double quotes for strings
  - Use trailing commas in multi-line structures
- **Modern Python (3.10+)**: Use `|` for unions, `match` statements, and `collections.abc` types
- **Always use type hints** with modern syntax: `dict[str, int]`, `list[User]`, `str | None`
- **Format with `ruff format`** (faster alternative to Black)
- **Use `pydantic` v2** for data validation and settings management

### Pythonic Code Patterns

**Leverage Python's Data Model:**

```python
# Implement special methods for natural behavior
class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vector2D({self.x!r}, {self.y!r})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
```

**Use Protocols for Duck Typing:**

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(obj: Drawable) -> None:  # Works with any object with draw()
    obj.draw()
```

**Prefer Generators and Iterators:**

```python
# Generator for memory efficiency
def read_large_file(path: str) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            yield line.strip()

# Generator expressions over list comprehensions when chaining
result = sum(x**2 for x in range(1_000_000))  # Memory efficient
```

**Use Right Collections:**

```python
from collections import defaultdict, Counter, deque

# Group items
groups: defaultdict[str, list[Item]] = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# Count efficiently
word_counts = Counter(words).most_common(10)

# Efficient queue operations
recent = deque(maxlen=100)  # Auto-discards old items
```

**Functional Tools:**

```python
from operator import attrgetter, itemgetter
from functools import partial

items.sort(key=attrgetter('price'))  # Not: lambda x: x.price
data.sort(key=itemgetter('name'))    # Not: lambda x: x['name']

# Partial application
quick_fetch = partial(fetch_data, timeout=5, retries=1)
```

**Pattern Matching (Python 3.10+):**

```python
def handle_event(event: dict[str, Any]) -> str:
    match event:
        case {"type": "login", "user_id": uid}:
            return f"User {uid} logged in"
        case {"type": "error", "code": code, "message": msg}:
            return f"Error {code}: {msg}"
        case _:
            return "Unknown event"
```

### Docstring Standards

Use Google-style docstrings for all public functions, classes, and modules:

```python
def calculate_discount(
    price: Decimal,
    discount_percent: float,
    min_amount: Decimal = Decimal("0.01")
) -> Decimal:
    """
    Calculate the discounted price for a product.

    Args:
        price: Original price of the product
        discount_percent: Discount percentage (0-100)
        min_amount: Minimum allowed final price

    Returns:
        Final price after applying discount

    Raises:
        ValueError: If discount_percent is not between 0 and 100
        ValueError: If final price would be below min_amount

    Example:
        >>> calculate_discount(Decimal("100"), 20)
        Decimal('80.00')
    """
```

### Naming Conventions

- **Variables and functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private attributes/methods**: `_leading_underscore`
- **Type aliases**: `PascalCase`
- **Enum values**: `UPPER_SNAKE_CASE`

## 🧪 Testing Strategy

### Test-Driven Development (TDD)

1. **Write the test first** - Define expected behavior before implementation
2. **Watch it fail** - Ensure the test actually tests something
3. **Write minimal code** - Just enough to make the test pass
4. **Refactor** - Improve code while keeping tests green
5. **Repeat** - One test at a time

### Testing Best Practices

```python
# Always use pytest fixtures for setup
import pytest
from datetime import datetime

@pytest.fixture
def sample_user():
    """Provide a sample user for testing."""
    return User(
        id=123,
        name="Test User",
        email="test@example.com",
        created_at=datetime.now()
    )

# Use descriptive test names
def test_user_can_update_email_when_valid(sample_user):
    """Test that users can update their email with valid input."""
    new_email = "newemail@example.com"
    sample_user.update_email(new_email)
    assert sample_user.email == new_email

# Test edge cases and error conditions
def test_user_update_email_fails_with_invalid_format(sample_user):
    """Test that invalid email formats are rejected."""
    with pytest.raises(ValidationError) as exc_info:
        sample_user.update_email("not-an-email")
    assert "Invalid email format" in str(exc_info.value)
```

### Test Organization

- Unit tests: Test individual functions/methods in isolation
- Integration tests: Test component interactions
- End-to-end tests: Test complete user workflows
- Keep test files next to the code they test
- Use `conftest.py` for shared fixtures
- Aim for 80%+ code coverage, but focus on critical paths

## 🚨 Error Handling

### Exception Best Practices

```python
# Create custom exceptions for your domain
class PaymentError(Exception):
    """Base exception for payment-related errors."""
    pass

class InsufficientFundsError(PaymentError):
    """Raised when account has insufficient funds."""
    def __init__(self, required: Decimal, available: Decimal):
        self.required = required
        self.available = available
        super().__init__(
            f"Insufficient funds: required {required}, available {available}"
        )

# Use specific exception handling
try:
    process_payment(amount)
except InsufficientFundsError as e:
    logger.warning(f"Payment failed: {e}")
    return PaymentResult(success=False, reason="insufficient_funds")
except PaymentError as e:
    logger.error(f"Payment error: {e}")
    return PaymentResult(success=False, reason="payment_error")

# Use context managers for resource management
from contextlib import contextmanager

@contextmanager
def database_transaction():
    """Provide a transactional scope for database operations."""
    conn = get_connection()
    trans = conn.begin_transaction()
    try:
        yield conn
        trans.commit()
    except Exception:
        trans.rollback()
        raise
    finally:
        conn.close()
```

### Logging Strategy

Use Loguru for simpler logging.

## 🔧 Configuration Management

### Environment Variables and Settings

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings with validation."""
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str
    redis_url: str = "redis://localhost:6379"
    api_key: str
    max_connections: int = 100

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()

# Usage
settings = get_settings()
```

## 🏗️ Data Models and Validation

### Pydantic v2 Patterns

```python
from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime
from decimal import Decimal

class ProductBase(BaseModel):
    """Base product model with modern v2 patterns."""
    name: str = Field(min_length=1, max_length=255)
    description: str | None = None  # Use | instead of Optional
    price: Decimal = Field(gt=0, decimal_places=2)
    category: str
    tags: list[str] = Field(default_factory=list)  # default_factory, not []

    @field_validator('price')  # Use field_validator, not @validator
    @classmethod
    def validate_price(cls, v: Decimal) -> Decimal:
        if v > Decimal('1000000'):
            raise ValueError('Price cannot exceed 1,000,000')
        return v

    @model_validator(mode='after')  # Multi-field validation
    def validate_model(self) -> "ProductBase":
        if "urgent" in self.tags and self.price > Decimal('10000'):
            raise ValueError('Urgent items cannot exceed $10,000')
        return self

    model_config = {
        'json_encoders': {Decimal: str},
        'frozen': False,
        'validate_assignment': True,
    }

class Product(ProductBase):
    """Complete product model with database fields."""
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool = True

    model_config = {
        **ProductBase.model_config,
        'from_attributes': True,  # Enable ORM mode
    }
```

## 🗄️ Database Naming Standards

### Entity-Specific Primary Keys

All database tables use entity-specific primary keys for clarity and consistency:

```sql
-- ✅ STANDARDIZED: Entity-specific primary keys
sessions.session_id UUID PRIMARY KEY
leads.lead_id UUID PRIMARY KEY
messages.message_id UUID PRIMARY KEY
daily_metrics.daily_metric_id UUID PRIMARY KEY
agencies.agency_id UUID PRIMARY KEY
````

### Field Naming Conventions

```sql
-- Primary keys: {entity}_id
session_id, lead_id, message_id

-- Foreign keys: {referenced_entity}_id
session_id REFERENCES sessions(session_id)
agency_id REFERENCES agencies(agency_id)

-- Timestamps: {action}_at
created_at, updated_at, started_at, expires_at

-- Booleans: is_{state}
is_connected, is_active, is_qualified

-- Counts: {entity}_count
message_count, lead_count, notification_count

-- Durations: {property}_{unit}
duration_seconds, timeout_minutes
```

### Model-Database Alignment

Models mirror database fields exactly to eliminate field mapping complexity:

```python
# ✅ STANDARDIZED: Models mirror database exactly
class Lead(BaseModel):
    lead_id: UUID = Field(default_factory=uuid4)  # Matches database field
    session_id: UUID                               # Matches database field
    agency_id: str                                 # Matches database field
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        alias_generator=None  # Use exact field names
    )
```

## 📝 Documentation Standards

### Code Documentation

- Every module should have a docstring explaining its purpose
- Public functions must have complete docstrings
- Complex logic should have inline comments with `# Reason:` prefix
- Keep README.md updated with setup instructions and examples
- Maintain CHANGELOG.md for version history

## 🚀 Performance & Concurrency

### Optimization Guidelines

- **Profile first**: Use `cProfile` or `py-spy` before optimizing
- **Cache wisely**: Use `@lru_cache` for expensive pure functions
- **Lazy evaluation**: Prefer generators over lists for large datasets
- **Right concurrency**: `asyncio` for I/O, `ProcessPoolExecutor` for CPU

### Performance Patterns

```python
from functools import lru_cache
from collections.abc import Iterator

# Cache expensive computations
@lru_cache(maxsize=1000)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Use generators for memory efficiency
def process_large_file(path: str) -> Iterator[dict]:
    """Lazy processing - never loads entire file."""
    with open(path) as f:
        for line in f:
            yield json.loads(line)
```

### Async/Concurrency Patterns

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor
from collections.abc import AsyncIterator

# Async iteration
class AsyncDataStream:
    async def __aiter__(self) -> "AsyncDataStream":
        return self

    async def __anext__(self) -> dict:
        data = await self.fetch_next()
        if data is None:
            raise StopAsyncIteration
        return data

# Async context managers
class AsyncResource:
    async def __aenter__(self) -> "AsyncResource":
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.disconnect()

# Gather with error handling
async def fetch_all(urls: list[str]) -> list[dict]:
    """Fetch all URLs concurrently."""
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks, return_exceptions=True)

# Mix sync/async with executors for CPU-bound work
async def cpu_heavy_work(data: list[int]) -> int:
    """Run CPU-intensive work in process pool."""
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, heavy_computation, data)
    return result
```

## 🛡️ Security Best Practices

### Security Guidelines

- Never commit secrets - use environment variables
- Validate all user input with Pydantic
- Use parameterized queries for database operations
- Implement rate limiting for APIs
- Use HTTPS for all external communications

### Example Security Implementation

```python
from passlib.context import CryptContext
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

def generate_secure_token(length: int = 32) -> str:
    """Generate a cryptographically secure random token."""
    return secrets.token_urlsafe(length)
```

## 📚 Useful Resources

### Essential Tools

- [UV Documentation](https://github.com/astral-sh/uv)
- [Ruff](https://github.com/astral-sh/ruff)
- [Pytest](https://docs.pytest.org/)
- [Pydantic](https://docs.pydantic.dev/)

### Python Best Practices

- [PEP 8](https://pep8.org/)
- [PEP 484 (Type Hints)](https://www.python.org/dev/peps/pep-0484/)

## ⚠️ Important Notes

- **NEVER ASSUME OR GUESS** - When in doubt, ask for clarification
- **Always verify file paths and module names** before use
- **Keep CLAUDE.md updated** when adding new patterns or dependencies
- **Test your code** - No feature is complete without tests
- **Document your decisions** - Future developers (including yourself) will thank you

## 🔍 Search Command Requirements

**CRITICAL**: Always use `rg` (ripgrep) instead of traditional `grep` and `find` commands:

```bash
# ❌ Don't use grep
grep -r "pattern" .

# ✅ Use rg instead
rg "pattern"

# ❌ Don't use find with name
find . -name "*.py"

# ✅ Use rg with file filtering
rg --files | rg "\.py$"
# or
rg --files -g "*.py"
```

**Enforcement Rules:**

```bash
(
    r"^grep\b(?!.*\|)",
    "Use 'rg' (ripgrep) instead of 'grep' for better performance and features",
),
(
    r"^find\s+\S+\s+-name\b",
    "Use 'rg --files | rg pattern' or 'rg --files -g pattern' instead of 'find -name' for better performance",
),
```

_This document is a living guide. Update it as the project evolves and new patterns emerge._
