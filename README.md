# TextCraft Utils (`textcraft-utils`)

[![CI/CD Pipeline](https://github.com/USHODAYA/TestPyPI-with-a-CI-CD-Pipeline/actions/workflows/publish.yml/badge.svg)](https://github.com/USHODAYA/TestPyPI-with-a-CI-CD-Pipeline/actions/workflows/publish.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage: 100%](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/USHODAYA/TestPyPI-with-a-CI-CD-Pipeline)
[![TestPyPI](https://img.shields.io/badge/TestPyPI-textcraft--utils-blue)](https://test.pypi.org/project/textcraft-utils/)

A robust, modern Python utility package for common text processing, string transformations, URL slug generation, word counting, truncation, and hashtag extraction. Built using the modern `pyproject.toml` standard (`PEP 517`/`PEP 621`), thoroughly tested with `pytest`, and automated with a GitHub Actions CI/CD release pipeline publishing to TestPyPI.

---

## 🌟 Features

- **`slugify(text, delimiter="-")`**: Converts arbitrary text to clean, URL-friendly slugs with configurable delimiters.
- **`count_words(text)`**: Accurately counts words while gracefully handling irregular whitespace and empty strings.
- **`to_uppercase(text)`**: Converts strings to clean uppercase format.
- **`truncate(text, max_length, suffix="...")`**: Truncates strings cleanly to specified boundaries with custom ellipsis/suffixes.
- **`extract_hashtags(text)`**: Extracts and deduplicates hashtag tokens from social and user-generated text.
- **Type Annotated**: Fully typed with Python type hints for great IDE autocomplete and static type checkers (`mypy`).
- **Comprehensive Test Suite**: Over 90% unit test coverage using `pytest` and `pytest-cov`.
- **Modern Packaging**: Configured with `pyproject.toml` and standard `src/` layout.

---

## 📁 Project Structure

```text
TestPyPI-with-a-CI-CD-Pipeline/
├── .github/
│   └── workflows/
│       └── publish.yml      # CI/CD pipeline (test + gated publish)
├── src/
│   └── textcraft_utils/
│       ├── __init__.py       # Package exports and version metadata
│       └── utils.py          # Public utility functions
├── tests/
│   ├── __init__.py
│   └── test_utils.py         # Pytest test suite (>90% coverage)
├── .gitignore                # Git ignore patterns
├── LICENSE                   # MIT License
├── pyproject.toml            # Modern project metadata and build configuration
└── README.md                 # Documentation
```

---

## 🚀 Installation

### Installing from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ textcraft-utils
```

### Installing from a Local Wheel

```bash
# Build the distribution packages
python -m build

# Install the generated wheel
pip install dist/textcraft_utils-0.0.1-py3-none-any.whl
```

### Local Development Installation

```bash
git clone https://github.com/USHODAYA/TestPyPI-with-a-CI-CD-Pipeline.git
cd TestPyPI-with-a-CI-CD-Pipeline
pip install -e ".[dev]"
```

---

## 💡 Quickstart & Usage

```python
from textcraft_utils import (
    slugify,
    count_words,
    to_uppercase,
    truncate,
    extract_hashtags,
)

# 1. Generate URL Slugs
print(slugify("Hello World! Welcome to Python 3"))
# Output: 'hello-world-welcome-to-python-3'

print(slugify("Custom Delimiter Example", delimiter="_"))
# Output: 'custom_delimiter_example'

# 2. Count Words
print(count_words("Modern CI/CD with TestPyPI and GitHub Actions"))
# Output: 7
print(count_words(""))
# Output: 0

# 3. Uppercase Conversion
print(to_uppercase("python packaging is awesome"))
# Output: 'PYTHON PACKAGING IS AWESOME'

# 4. Truncate Strings
print(truncate("Continuous Integration and Continuous Deployment", 25))
# Output: 'Continuous Integration...'

# 5. Extract Hashtags
print(extract_hashtags("Loving the new #python release! Check out #devops and #Python"))
# Output: ['python', 'devops']
```

---

## 🧪 Running Unit Tests & Coverage

Run tests using `pytest` with coverage report:

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=90
```

---

## 📦 Building Distribution Artifacts

Build both source distribution (`.tar.gz`) and binary wheel (`.whl`):

```bash
python -m build
```

The resulting artifacts are placed into the `dist/` directory:
- `dist/textcraft_utils-0.0.1-py3-none-any.whl` (Wheel)
- `dist/textcraft-utils-0.0.1.tar.gz` (Source Distribution)

Verify packages with `twine`:

```bash
twine check dist/*
```

---

## 🔄 CI/CD Release Pipeline (GitHub Actions)

The workflow defined in `.github/workflows/publish.yml` executes two stages:

1. **`test` Job**:
   - Triggers on every `push` to `main` and every `pull_request` targeting `main`.
   - Sets up Python, installs dependencies, and runs `pytest` ensuring $\ge 90\%$ code coverage.

2. **`publish` Job**:
   - Gated via `needs: test`. Only runs if all tests pass.
   - Triggers **only** when a git version tag is pushed matching `v*` (e.g., `v0.0.1`, `v1.0.0`).
   - Securely accesses `secrets.TEST_PYPI_API_TOKEN` to publish the artifacts to TestPyPI using `twine`.

### How to Trigger a Release

```bash
# Tag a new release
git tag v0.0.1

# Push the tag to GitHub
git push origin v0.0.1
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
