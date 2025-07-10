#!/usr/bin/env python3
"""
Comprehensive Demo: All Linked List Techniques

This script demonstrates all three linked list techniques:
1. Multiple Pass Technique
2. Slow-Fast Pointer Technique
3. Temporary Head Technique

Run this to see all techniques in action with a unified example.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import (
    MultiplePassLinkedList,
    SlowFastLinkedList,
    TemporaryHeadLinkedList
)

def demo_all_techniques():
    """Demonstrate all linked list techniques"""
    print("=" * 70)
    print("COMPREHENSIVE LINKED LIST TECHNIQUES DEMO")
    print("=" * 70)

    # Common test data
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("\n" + "="*70)
    print("1. MULTIPLE PASS TECHNIQUE - Finding Middle Element")
    print("="*70)

    mp_list = MultiplePassLinkedList()
    for item in test_data:
        mp_list.append(item)

    print("List: ", end="")
    mp_list.print_list()

    middle = mp_list.find_middle()
    print(f"Middle element: {middle}")

    # Test with different lengths
    print("\nTesting with different lengths:")
    for length in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        temp_list = MultiplePassLinkedList()
        for i in range(1, length + 1):
            temp_list.append(i)
        middle = temp_list.find_middle()
        print(f"Length {length:2d}: Middle = {middle}")

    print("\n" + "="*70)
    print("2. SLOW-FAST POINTER TECHNIQUE - Cycle Detection")
    print("="*70)

    sf_list = SlowFastLinkedList()
    for item in test_data:
        sf_list.append(item)

    print("List without cycle: ", end="")
    sf_list.print_list()

    result = sf_list.find_cycle_start()
    print(f"Cycle detected: {result is not None}")

    # Create cycle and test
    print("\nCreating cycle: last node (10) -> node at position 3 (value 4)")
    sf_list.create_cycle(3)
    print("List now has a cycle (cannot print safely)")

    result = sf_list.find_cycle_start()
    print(f"Cycle starts at node with value: {result}")

    # Test different cycle positions
    print("\nTesting cycles at different positions:")
    for cycle_pos in [0, 2, 4, 6, 8]:
        test_list = SlowFastLinkedList()
        for i in range(1, 11):
            test_list.append(i)

        test_list.create_cycle(cycle_pos)
        result = test_list.find_cycle_start()
        expected_value = cycle_pos + 1
        print(f"Cycle at position {cycle_pos}: detected value {result} (expected {expected_value})")

    print("\n" + "="*70)
    print("3. TEMPORARY HEAD TECHNIQUE - Deletion and Reversal")
    print("="*70)

    th_list = TemporaryHeadLinkedList()
    for item in test_data:
        th_list.append(item)

    print("Original list: ", end="")
    th_list.print_list()

    # Demonstrate deletions
    print("\nDemonstrating deletions:")
    deletions = [5, 1, 10, 3, 7]  # middle, head, tail, etc.
    for value in deletions:
        print(f"Deleting {value}: ", end="")
        th_list.delete_node(value)
        th_list.print_list()

    # Demonstrate reversal
    print("\nDemonstrating reversal:")
    print("Before reversal: ", end="")
    th_list.print_list()

    th_list.reverse()
    print("After reversal: ", end="")
    th_list.print_list()

    th_list.reverse()
    print("After second reversal: ", end="")
    th_list.print_list()

    print("\n" + "="*70)
    print("4. PERFORMANCE COMPARISON")
    print("="*70)

    print("Algorithm Complexities:")
    print("┌─────────────────────────────┬─────────────┬─────────────┐")
    print("│ Technique                   │ Time        │ Space       │")
    print("├─────────────────────────────┼─────────────┼─────────────┤")
    print("│ Multiple Pass (find middle) │ O(n)        │ O(1)        │")
    print("│ Slow-Fast (cycle detection) │ O(n)        │ O(1)        │")
    print("│ Temporary Head (deletion)   │ O(n)        │ O(1)        │")
    print("│ Temporary Head (reversal)   │ O(n)        │ O(1)        │")
    print("└─────────────────────────────┴─────────────┴─────────────┘")

    print("\n" + "="*70)
    print("5. WHEN TO USE EACH TECHNIQUE")
    print("="*70)

    print("Multiple Pass Technique:")
    print("  ✓ When you need to find middle element")
    print("  ✓ When you need to know list length first")
    print("  ✓ When memory is limited (constant space)")
    print("  ✗ When you want to minimize traversals")

    print("\nSlow-Fast Pointer Technique:")
    print("  ✓ Cycle detection in linked lists")
    print("  ✓ Finding middle element in one pass")
    print("  ✓ Detecting loops in any sequential structure")
    print("  ✗ When list might be very short (overhead)")

    print("\nTemporary Head Technique:")
    print("  ✓ Simplifying deletion operations")
    print("  ✓ Handling edge cases elegantly")
    print("  ✓ List reversal with uniform code")
    print("  ✓ When head node might be modified")
    print("  ✗ When memory is extremely constrained")

    print("\n" + "="*70)
    print("DEMO COMPLETE")
    print("="*70)

if __name__ == "__main__":
    demo_all_techniques()
