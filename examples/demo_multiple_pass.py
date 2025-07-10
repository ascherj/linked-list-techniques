#!/usr/bin/env python3
"""
Demo: Multiple Pass Technique for Finding Middle Element

This example demonstrates the multiple pass technique for finding the middle
element of a linked list. The algorithm makes two passes through the list:
1. First pass: Count the total number of nodes
2. Second pass: Traverse to the middle position
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.multiple_pass import MultiplePassLinkedList

def demo_multiple_pass():
    """Demonstrate the multiple pass technique"""
    print("=" * 60)
    print("MULTIPLE PASS TECHNIQUE DEMO")
    print("=" * 60)

    # Create a linked list
    llist = MultiplePassLinkedList()

    print("\n1. Building linked list step by step:")
    print("-" * 40)
    for i in range(1, 8):
        llist.append(i)
        middle = llist.find_middle()
        print(f"List with {len(llist)} element(s): {llist}")
        print(f"   Middle element: {middle}")

    print("\n2. Testing with different data types:")
    print("-" * 40)

    # String example
    string_list = MultiplePassLinkedList()
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    for word in words:
        string_list.append(word)

    print(f"String list: {string_list}")
    print(f"Middle element: {string_list.find_middle()}")

    # Mixed data types
    mixed_list = MultiplePassLinkedList()
    mixed_data = [1, "hello", 3.14, [1, 2, 3], {"key": "value"}]
    for item in mixed_data:
        mixed_list.append(item)

    print(f"Mixed data list: {mixed_list}")
    print(f"Middle element: {mixed_list.find_middle()}")

    print("\n3. Edge cases:")
    print("-" * 40)

    # Empty list
    empty_list = MultiplePassLinkedList()
    print("Empty list middle:", empty_list.find_middle())

    # Single element
    single_list = MultiplePassLinkedList()
    single_list.append(42)
    print(f"Single element list: {single_list}")
    print(f"Middle element: {single_list.find_middle()}")

    print("\n4. Algorithm explanation:")
    print("-" * 40)
    print("The multiple pass technique works by:")
    print("1. First pass: Count total nodes (O(n))")
    print("2. Calculate middle position: count // 2")
    print("3. Second pass: Traverse to middle position (O(n))")
    print("4. Total time complexity: O(n)")
    print("5. Space complexity: O(1)")

if __name__ == "__main__":
    demo_multiple_pass()
