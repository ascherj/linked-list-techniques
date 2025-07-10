# Linked List Unit Tests

The `tests/` directory contains comprehensive unit tests for the linked list implementations demonstrating various algorithmic techniques.

## Test Structure

### 1. `tests/test_linked_list_base.py` (9 tests)
Tests for the base `LinkedList` and `Node` classes from `src/linked_list_base.py`:
- Node creation and linking
- List creation and append functionality
- Print list functionality with various data types
- Edge cases (empty lists, single elements)

### 2. `tests/test_multiple_pass.py` (10 tests)
Tests for the `MultiplePassLinkedList` class from `src/multiple_pass.py`:
- Finding middle element in lists of various lengths
- Edge cases (empty, single element, two elements)
- Odd and even length lists
- Different data types (strings, mixed types)
- Verification of the two-pass algorithm

### 3. `tests/test_slow_fast.py` (14 tests)
Tests for the `SlowFastLinkedList` class from `src/slow_fast.py`:
- Cycle detection using Floyd's algorithm
- Cycle creation at various positions
- Edge cases (empty list, single element, no cycle)
- Invalid cycle positions
- Different data types
- Comprehensive cycle detection scenarios

### 4. `tests/test_temporary_head.py` (20 tests)
Tests for the `TemporaryHeadLinkedList` class from `src/temporary_head.py`:
- Node deletion (head, middle, tail, non-existent)
- List reversal (empty, single, multiple elements)
- Combined operations (delete then reverse, reverse then delete)
- Edge cases and error conditions
- Different data types
- Temporary head technique verification

## Running Tests

### Run Individual Test Files
```bash
# Run specific test file (from project root)
python -m unittest tests.test_linked_list_base -v
python -m unittest tests.test_multiple_pass -v
python -m unittest tests.test_slow_fast -v
python -m unittest tests.test_temporary_head -v
```

### Run All Tests
```bash
# Run comprehensive test suite (from project root)
python tests/run_all_tests.py
```

The test runner provides:
- Individual test results for each module
- Detailed output for any failures
- Summary with total counts
- Pass/fail status for each module

## Test Coverage

Total: **53 tests** covering:
- ✅ Core functionality (Node, LinkedList base)
- ✅ Multiple pass technique (finding middle element)
- ✅ Slow-fast pointer technique (cycle detection)
- ✅ Temporary head technique (deletion and reversal)
- ✅ Edge cases and error conditions
- ✅ Various data types (integers, strings, mixed)
- ✅ Algorithm verification and correctness

## Test Features

- **Comprehensive coverage**: Tests all public methods and edge cases
- **Clear documentation**: Each test has descriptive docstrings
- **Helper methods**: Utility functions for easier testing
- **Data validation**: Tests with various data types and structures
- **Algorithm verification**: Tests confirm correct algorithmic behavior
- **Error handling**: Tests for invalid inputs and edge cases

## Relationship to Other Components

The testing ecosystem works together with other project components:

### Tests vs Usage Sections vs Demo Files

| Component | Purpose | Scope | Audience |
|-----------|---------|--------|----------|
| **Unit Tests** (`tests/`) | Verify correctness | Exhaustive edge cases | Developers/QA |
| **Usage Sections** (`src/*.py`) | Quick functionality check | Basic operations | Developers |
| **Demo Files** (`examples/`) | Educational demonstration | Comprehensive learning | Students/learners |

### Example Workflow
1. **Unit Tests** ensure the code works correctly
2. **Usage Sections** provide quick verification during development
3. **Demo Files** teach concepts and show practical applications

## File Dependencies

```
tests/test_linked_list_base.py → src/linked_list_base.py
tests/test_multiple_pass.py → src/multiple_pass.py → src/linked_list_base.py
tests/test_slow_fast.py → src/slow_fast.py → src/linked_list_base.py
tests/test_temporary_head.py → src/temporary_head.py → src/linked_list_base.py
tests/run_all_tests.py → all test files
```

## Project Structure Context

The tests are part of the organized project structure:
```
├── src/                    # Source code being tested
├── tests/                  # Unit tests (this directory)
├── examples/               # Demo scripts showing usage
├── docs/                   # Documentation (including this file)
└── README.md              # Main project documentation
```

All tests are designed to be independent and can be run in any order.
