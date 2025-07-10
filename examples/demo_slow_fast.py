#!/usr/bin/env python3
"""
Demo: Slow-Fast Pointer Technique for Cycle Detection

This example demonstrates Floyd's cycle detection algorithm using slow and fast
pointers. The algorithm detects cycles in linked lists and finds the start of
the cycle using a two-phase approach.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.slow_fast import SlowFastLinkedList

def demo_slow_fast():
    """Demonstrate the slow-fast pointer technique"""
    print("=" * 60)
    print("SLOW-FAST POINTER TECHNIQUE DEMO")
    print("=" * 60)

    print("\n1. Testing cycle detection without cycles:")
    print("-" * 50)

    # Test without cycle
    llist = SlowFastLinkedList()
    for i in range(1, 6):
        llist.append(i)

    print(f"List: {llist}")
    result = llist.find_cycle_start()
    print(f"Cycle detected: {result is not None}")
    if result:
        print(f"Cycle starts at: {result}")

    print("\n2. Testing cycle detection with cycles:")
    print("-" * 50)

    # Test with cycle at different positions
    test_cases = [
        (5, 0, "Cycle: last node -> first node"),
        (5, 1, "Cycle: last node -> second node"),
        (5, 2, "Cycle: last node -> third node"),
        (5, 4, "Cycle: last node -> last node (self-loop)"),
        (7, 3, "Cycle: last node -> fourth node"),
    ]

    for length, cycle_pos, description in test_cases:
        test_list = SlowFastLinkedList()
        for i in range(1, length + 1):
            test_list.append(i)

        print(f"\n{description}")
        print(f"Original list: 1 -> 2 -> ... -> {length} -> None")

        success = test_list.create_cycle(cycle_pos)
        result = test_list.find_cycle_start()

        if success and result is not None:
            print(f"✅ Cycle detected! Starts at node with value: {result}")
        else:
            print("❌ No cycle detected")

    print("\n3. Testing with different data types:")
    print("-" * 50)

    # String data
    string_list = SlowFastLinkedList()
    words = ["apple", "banana", "cherry", "date"]
    for word in words:
        string_list.append(word)

    print("String list: apple -> banana -> cherry -> date -> None")
    string_list.create_cycle(1)  # date -> banana
    result = string_list.find_cycle_start()
    print(f"Cycle starts at: {result}")

    print("\n4. Edge cases:")
    print("-" * 50)

    # Empty list
    empty_list = SlowFastLinkedList()
    print("Empty list cycle detection:", empty_list.find_cycle_start())

    # Single element
    single_list = SlowFastLinkedList()
    single_list.append(42)
    print("Single element cycle detection:", single_list.find_cycle_start())

    # Two elements with cycle
    two_list = SlowFastLinkedList()
    two_list.append(1)
    two_list.append(2)
    two_list.create_cycle(0)  # 2 -> 1
    print("Two element cycle detection:", two_list.find_cycle_start())

    print("\n5. Algorithm explanation:")
    print("-" * 50)
    print("Floyd's cycle detection algorithm (Tortoise and Hare):")
    print("Phase 1: Detection")
    print("  - Slow pointer moves 1 step at a time")
    print("  - Fast pointer moves 2 steps at a time")
    print("  - If there's a cycle, they will eventually meet")
    print("Phase 2: Finding cycle start")
    print("  - Reset slow pointer to head")
    print("  - Move both pointers at same speed")
    print("  - They meet at the cycle start")
    print("Time complexity: O(n)")
    print("Space complexity: O(1)")

if __name__ == "__main__":
    demo_slow_fast()
