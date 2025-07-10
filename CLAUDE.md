# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational Python project implementing linked list data structures with three key algorithmic techniques:

1. **Multiple Pass Technique** - Finding middle elements through two-pass traversal
2. **Slow-Fast Pointer Technique** - Cycle detection using Floyd's algorithm
3. **Temporary Head Technique** - Simplified deletion and reversal using dummy nodes

## Common Development Commands

### Testing
```bash
# Run all tests (53 total tests across 4 modules)
python tests/run_all_tests.py

# Run specific test modules
python -m unittest tests.test_linked_list_base -v
python -m unittest tests.test_multiple_pass -v
python -m unittest tests.test_slow_fast -v
python -m unittest tests.test_temporary_head -v
```

### Running Examples
```bash
# Run comprehensive demo of all techniques
python examples/demo_all.py

# Run individual technique demos
python examples/demo_multiple_pass.py
python examples/demo_slow_fast.py
python examples/demo_temporary_head.py
```

### Running Source Files Directly
```bash
# Each technique file can be run independently for quick testing
# Note: Must use -m flag due to relative imports
python -m src.multiple_pass
python -m src.slow_fast
python -m src.temporary_head
```

## Architecture

### Core Structure
- **Base Classes**: `Node` and `LinkedList` in `src/linked_list_base.py` provide fundamental linked list operations
- **Enhanced Base Features**: `LinkedList` includes `__len__()`, `__str__()`, and comprehensive type hints
- **Technique Classes**: Each technique inherits from `LinkedList` and adds specialized methods
- **Import Pattern**: All classes are accessible via `from src import ClassName`
- **Type Safety**: Full type hints throughout using `typing.Optional` and `typing.Any`

### Class Hierarchy
```
LinkedList (base)
├── MultiplePassLinkedList
├── SlowFastLinkedList  
└── TemporaryHeadLinkedList
```

### Key Methods by Technique

**LinkedList (Base Class)**:
- `append(data: Any) -> None` - Add node to end of list
- `print_list() -> None` - Print list in readable format
- `__len__() -> int` - Get number of nodes (enables `len(list)`)
- `__str__() -> str` - String representation (enables `str(list)`)

**MultiplePassLinkedList**:
- `find_middle() -> Optional[Any]` - Two-pass algorithm to find middle element

**SlowFastLinkedList**:
- `find_cycle_start() -> Optional[Any]` - Detects and returns cycle start using Floyd's algorithm
- `create_cycle(pos: int) -> bool` - Creates cycle at specified position, returns success status

**TemporaryHeadLinkedList**:
- `delete_node(value: Any) -> bool` - Deletes node using dummy head, returns True if successful
- `reverse() -> None` - Reverses list using temporary head technique

### Testing Architecture
- **53 total tests** across 4 test modules
- Each test module corresponds to a source file
- `tests/run_all_tests.py` provides comprehensive test execution with detailed reporting
- Tests cover functionality, edge cases, different data types, and algorithm correctness

### Package Structure
All classes are exported through `src/__init__.py` with proper `__all__` declarations. Import any class directly:
```python
from src import LinkedList, MultiplePassLinkedList, SlowFastLinkedList, TemporaryHeadLinkedList
```

## Code Patterns

### Type Hints
All code uses comprehensive type hints for better IDE support and code clarity:
```python
from typing import Optional, Any

def find_middle(self) -> Optional[Any]:
    """Find middle element with proper type annotations."""
    
def delete_node(self, value: Any) -> bool:
    """Delete node and return success status."""
```

### Relative Imports
Source files use relative imports: `from .linked_list_base import LinkedList`

### Path Management
Examples and tests add parent directory to path for imports:
```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
```

### Testing Pattern
Each technique file includes executable usage examples in `if __name__ == "__main__":` blocks that provide quick validation of core functionality. These are simplified for developer use, while comprehensive educational examples are in the `examples/` directory.

### Enhanced APIs
Methods now return meaningful values where appropriate:
- `delete_node()` returns `bool` for success/failure
- `create_cycle()` returns `bool` for success/failure
- Base class supports `len()` and `str()` built-in functions

## Algorithm Complexities

All implemented algorithms maintain:
- **Time Complexity**: O(n) 
- **Space Complexity**: O(1)

This is an educational project focused on demonstrating algorithmic techniques rather than production code, with emphasis on clear, readable implementations, comprehensive testing, and modern Python practices including type safety and comprehensive documentation.
