# Linked List Techniques Implementation

A comprehensive implementation of linked list data structures demonstrating three key algorithmic techniques: Multiple Pass, Slow-Fast Pointer, and Temporary Head.

## 🚀 Quick Start

```bash
# Run all examples
python examples/demo_all.py

# Run specific technique demos
python examples/demo_multiple_pass.py
python examples/demo_slow_fast.py
python examples/demo_temporary_head.py

# Run all tests
python tests/run_all_tests.py
```

## 📁 Project Structure

```
.
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── linked_list_base.py      # Base Node and LinkedList classes
│   ├── multiple_pass.py         # Multiple pass technique implementation
│   ├── slow_fast.py             # Slow-fast pointer technique implementation
│   └── temporary_head.py        # Temporary head technique implementation
├── tests/                        # Unit tests
│   ├── __init__.py              # Test package initialization
│   ├── test_linked_list_base.py # Base class tests (9 tests)
│   ├── test_multiple_pass.py    # Multiple pass tests (10 tests)
│   ├── test_slow_fast.py        # Slow-fast pointer tests (14 tests)
│   ├── test_temporary_head.py   # Temporary head tests (20 tests)
│   └── run_all_tests.py         # Test runner (53 total tests)
├── examples/                     # Demo scripts
│   ├── demo_multiple_pass.py    # Multiple pass technique demo
│   ├── demo_slow_fast.py        # Slow-fast pointer technique demo
│   ├── demo_temporary_head.py   # Temporary head technique demo
│   └── demo_all.py              # Comprehensive demo
├── docs/                         # Documentation
│   └── README_TESTS.md          # Test documentation
└── README.md                    # This file
```

## 🎯 Techniques Implemented

### 1. Multiple Pass Technique
**Purpose**: Find the middle element of a linked list
**Algorithm**: Two-pass approach - count nodes, then traverse to middle
**Time Complexity**: O(n) | **Space Complexity**: O(1)

```python
from src import MultiplePassLinkedList

llist = MultiplePassLinkedList()
for i in range(1, 6):
    llist.append(i)

middle = llist.find_middle()  # Returns 3
```

### 2. Slow-Fast Pointer Technique (Floyd's Algorithm)
**Purpose**: Detect cycles in linked lists
**Algorithm**: Two pointers moving at different speeds
**Time Complexity**: O(n) | **Space Complexity**: O(1)

```python
from src import SlowFastLinkedList

llist = SlowFastLinkedList()
for i in range(1, 6):
    llist.append(i)

llist.create_cycle(1)  # Create cycle: 5 -> 2
cycle_start = llist.find_cycle_start()  # Returns 2
```

### 3. Temporary Head Technique
**Purpose**: Simplify deletion and reversal operations
**Algorithm**: Use dummy node to handle edge cases
**Time Complexity**: O(n) | **Space Complexity**: O(1)

```python
from src import TemporaryHeadLinkedList

llist = TemporaryHeadLinkedList()
for i in range(1, 6):
    llist.append(i)

llist.delete_node(1)  # Delete head - simplified with dummy node
llist.reverse()       # Reverse list using temporary head
```

## 🧪 Testing

The project includes comprehensive unit tests with **53 total tests** covering:

- ✅ Core functionality and edge cases
- ✅ Algorithm correctness verification
- ✅ Different data types (integers, strings, mixed)
- ✅ Error handling and invalid inputs
- ✅ Performance characteristics

```bash
# Run all tests with detailed output
python tests/run_all_tests.py

# Run specific test modules
python -m unittest tests.test_multiple_pass -v
python -m unittest tests.test_slow_fast -v
python -m unittest tests.test_temporary_head -v
```

## 📊 Performance Comparison

| Technique | Operation | Time | Space | Use Case |
|-----------|-----------|------|-------|----------|
| Multiple Pass | Find Middle | O(n) | O(1) | When you need exact middle |
| Slow-Fast | Cycle Detection | O(n) | O(1) | Detect loops/cycles |
| Slow-Fast | Find Middle | O(n) | O(1) | One-pass middle finding |
| Temporary Head | Deletion | O(n) | O(1) | Simplified edge cases |
| Temporary Head | Reversal | O(n) | O(1) | Clean reversal logic |

## 🔧 Usage Examples

### Basic Usage
```python
# Import all classes
from src import (
    LinkedList,
    MultiplePassLinkedList,
    SlowFastLinkedList,
    TemporaryHeadLinkedList
)

# Create and populate lists
llist = MultiplePassLinkedList()
for i in range(1, 6):
    llist.append(i)

# Use specific techniques
middle = llist.find_middle()
```

### Advanced Usage
```python
# Cycle detection example
cycle_list = SlowFastLinkedList()
for i in range(1, 8):
    cycle_list.append(i)

cycle_list.create_cycle(2)  # Create cycle at position 2
if cycle_list.find_cycle_start():
    print("Cycle detected!")
```

## 🎓 Educational Value

This implementation demonstrates:

1. **Algorithm Design Patterns**: Common techniques used in competitive programming
2. **Edge Case Handling**: Proper handling of empty lists, single elements, etc.
3. **Code Organization**: Clean separation of concerns and modular design
4. **Testing Practices**: Comprehensive unit testing with edge cases
5. **Documentation**: Clear explanations and usage examples

## 🤝 Contributing

1. All code follows Python best practices
2. Comprehensive tests are required for new features
3. Documentation should be updated for any changes
4. Examples should demonstrate real-world usage

## 📚 Further Reading

- [Floyd's Cycle Detection Algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare)
- [Linked List Techniques](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [Two Pointer Technique](https://www.geeksforgeeks.org/two-pointers-technique/)
