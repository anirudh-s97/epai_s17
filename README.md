# Python Dictionary Operations Assignments

This repository contains two assignments focused on dictionary operations in Python:

## Assignment 1: Dictionary Structure Validation

### Overview
Implement a validator that checks if a nested dictionary matches a given template structure. This is commonly used in API data validation scenarios.

### Features
- Validates dictionary structure against a template
- Checks for:
  - Missing keys
  - Extra keys
  - Incorrect data types
- Provides detailed error messages with path to problematic keys
- Handles nested dictionaries of arbitrary depth

### Function Signature
```python
def validate(data: dict, template: dict) -> tuple[bool, str]:
    """
    Validates dictionary structure against a template.
    
    Returns:
    - tuple: (is_valid: bool, error_message: str)
    """
```

### Running Tests
```bash
pytest test_validate.py
```

## Assignment 2: Word Frequency Dictionary Merger

### Overview
Implement functions to merge word frequency dictionaries from multiple sources, simulating data aggregation from distributed servers.

### Features
- Two implementation approaches:
  - Using `collections.defaultdict`
  - Using `collections.Counter`
- Optional bonus: Sort results by frequency
- Handles arbitrary number of input dictionaries
- Maintains data integrity during merging

### Function Signatures
```python
def merge_with_defaultdict(*dicts) -> dict:
    """
    Merges dictionaries using defaultdict
    """

def merge_with_counter(*dicts) -> dict:
    """
    Merges dictionaries using Counter
    """
```

### Running Tests
```bash
pytest test_merge.py
```

## Project Structure
```
.
├── README.md
├── .github/
│   └── workflows/
│       └── pytest.yml
├── student_code.py      # Assignment 1 implementation
├── student_merge.py     # Assignment 2 implementation
├── test_validate.py     # Tests for Assignment 1
└── test_merge.py       # Tests for Assignment 2
```

## GitHub Actions Configuration
The repository uses GitHub Actions to automatically run tests on push and pull requests. The workflow:
- Sets up Python environment
- Installs dependencies
- Runs pytest for both assignments
- Reports test results

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install dependencies:
```bash
pip install pytest
```

3. Run tests locally:
```bash
# Run all tests
pytest

# Run specific assignment tests
pytest test_validate.py
pytest test_merge.py
```

## Requirements
- Python 3.x
- pytest
- collections (standard library)

## Note
- All keys in templates are required
- No extra keys are permitted
- Lists are not included as possible values
- Error messages must match exact format specified in tests# epai_s17
