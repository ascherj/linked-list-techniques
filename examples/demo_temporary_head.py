#!/usr/bin/env python3
"""
Demo: Temporary Head Technique for Deletion and Reversal

This example demonstrates the temporary head (dummy node) technique for
simplifying linked list operations like deletion and reversal. The technique
uses a dummy node to handle edge cases more elegantly.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.temporary_head import TemporaryHeadLinkedList

def demo_temporary_head():
    """Demonstrate the temporary head technique"""
    print("=" * 60)
    print("TEMPORARY HEAD TECHNIQUE DEMO")
    print("=" * 60)

    print("\n1. Demonstrating node deletion:")
    print("-" * 40)

    # Create initial list
    llist = TemporaryHeadLinkedList()
    for i in range(1, 6):
        llist.append(i)

    print(f"Original list: {llist}")

    # Delete middle element
    print("\nDeleting middle element (3):")
    success = llist.delete_node(3)
    print(f"Deleted: {success}, List: {llist}")

    # Delete head element
    print("\nDeleting head element (1):")
    success = llist.delete_node(1)
    print(f"Deleted: {success}, List: {llist}")

    # Delete tail element
    print("\nDeleting tail element (5):")
    success = llist.delete_node(5)
    print(f"Deleted: {success}, List: {llist}")

    # Try to delete non-existent element
    print("\nTrying to delete non-existent element (99):")
    success = llist.delete_node(99)
    print(f"Deleted: {success}, List: {llist}")

    print("\n2. Demonstrating list reversal:")
    print("-" * 40)

    # Create a fresh list for reversal demo
    rev_list = TemporaryHeadLinkedList()
    for i in range(1, 6):
        rev_list.append(i)

    print(f"Original list: {rev_list}")

    print("Reversing list...")
    rev_list.reverse()
    print(f"After reversal: {rev_list}")

    print("Reversing again (should return to original)...")
    rev_list.reverse()
    print(f"After second reversal: {rev_list}")

    print("\n3. Edge cases:")
    print("-" * 40)

    # Empty list operations
    empty_list = TemporaryHeadLinkedList()
    print("Empty list operations:")
    print(f"  Before: {empty_list}")

    success = empty_list.delete_node(1)
    print(f"  After delete attempt: {success}, List: {empty_list}")

    empty_list.reverse()
    print(f"  After reverse attempt: {empty_list}")

    # Single element operations
    single_list = TemporaryHeadLinkedList()
    single_list.append(42)
    print("\nSingle element operations:")
    print(f"  Before: {single_list}")

    single_list.reverse()
    print(f"  After reverse: {single_list}")

    success = single_list.delete_node(42)
    print(f"  After delete: {success}, List: {single_list}")

    print("\n4. Combined operations:")
    print("-" * 40)

    combined_list = TemporaryHeadLinkedList()
    for i in range(1, 8):
        combined_list.append(i)

    print(f"Starting list: {combined_list}")

    # Delete some elements
    combined_list.delete_node(3)
    combined_list.delete_node(6)
    print(f"After deleting 3 and 6: {combined_list}")

    # Reverse
    combined_list.reverse()
    print(f"After reversing: {combined_list}")

    # Delete head and tail
    combined_list.delete_node(7)  # New head after reverse
    combined_list.delete_node(1)  # New tail after reverse
    print(f"After deleting new head and tail: {combined_list}")

    print("\n5. Different data types:")
    print("-" * 40)

    # String data
    string_list = TemporaryHeadLinkedList()
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    for word in words:
        string_list.append(word)

    print(f"String list: {string_list}")

    success = string_list.delete_node("cherry")
    print(f"After deleting 'cherry': {success}, List: {string_list}")

    string_list.reverse()
    print(f"After reversing: {string_list}")

    print("\n6. Algorithm explanation:")
    print("-" * 40)
    print("Temporary head technique benefits:")
    print("1. Simplifies edge case handling (empty list, single element)")
    print("2. Eliminates special cases for head operations")
    print("3. Makes code more uniform and easier to understand")
    print("4. Reduces bugs related to pointer manipulation")
    print("\nFor deletion:")
    print("  - Create dummy node pointing to head")
    print("  - Use dummy as starting point for traversal")
    print("  - Update head from dummy.next at the end")
    print("\nFor reversal:")
    print("  - Use dummy node as initial 'previous' pointer")
    print("  - Simplifies the reversal logic")
    print("  - Handle the final pointer cleanup")

if __name__ == "__main__":
    demo_temporary_head()
