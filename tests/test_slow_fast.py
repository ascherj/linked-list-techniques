import unittest
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.slow_fast import SlowFastLinkedList


class TestSlowFastLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.llist = SlowFastLinkedList()

    def test_find_cycle_start_empty_list(self):
        """Test cycle detection on empty list"""
        result = self.llist.find_cycle_start()
        self.assertIsNone(result)

    def test_find_cycle_start_single_element(self):
        """Test cycle detection on single element list"""
        self.llist.append(1)
        result = self.llist.find_cycle_start()
        self.assertIsNone(result)

    def test_find_cycle_start_no_cycle(self):
        """Test cycle detection on list without cycle"""
        for i in range(1, 6):
            self.llist.append(i)

        result = self.llist.find_cycle_start()
        self.assertIsNone(result)

    def test_create_cycle_invalid_position(self):
        """Test creating cycle with invalid position"""
        for i in range(1, 4):
            self.llist.append(i)

        # Test negative position
        self.llist.create_cycle(-1)
        result = self.llist.find_cycle_start()
        self.assertIsNone(result)

        # Test position beyond list length
        self.llist.create_cycle(10)
        result = self.llist.find_cycle_start()
        self.assertIsNone(result)

    def test_create_cycle_at_head(self):
        """Test creating cycle that points back to head"""
        for i in range(1, 4):
            self.llist.append(i)

        # Create cycle: 3 -> 1 (position 0)
        self.llist.create_cycle(0)
        result = self.llist.find_cycle_start()
        self.assertEqual(result, 1)

    def test_create_cycle_at_middle(self):
        """Test creating cycle that points to middle element"""
        for i in range(1, 6):
            self.llist.append(i)

        # Create cycle: 5 -> 2 (position 1)
        self.llist.create_cycle(1)
        result = self.llist.find_cycle_start()
        self.assertEqual(result, 2)

    def test_create_cycle_at_last_element(self):
        """Test creating cycle that points to last element (self-loop)"""
        for i in range(1, 4):
            self.llist.append(i)

        # Create cycle: 3 -> 3 (position 2, self-loop)
        self.llist.create_cycle(2)
        result = self.llist.find_cycle_start()
        self.assertEqual(result, 3)

    def test_cycle_detection_various_positions(self):
        """Test cycle detection with various cycle positions"""
        test_cases = [
            (5, 0, 1),  # 5 elements, cycle to position 0, expect data 1
            (5, 1, 2),  # 5 elements, cycle to position 1, expect data 2
            (5, 2, 3),  # 5 elements, cycle to position 2, expect data 3
            (5, 3, 4),  # 5 elements, cycle to position 3, expect data 4
            (5, 4, 5),  # 5 elements, cycle to position 4, expect data 5
        ]

        for length, cycle_pos, expected_data in test_cases:
            with self.subTest(length=length, cycle_pos=cycle_pos):
                # Create new list for each test
                test_list = SlowFastLinkedList()
                for i in range(1, length + 1):
                    test_list.append(i)

                test_list.create_cycle(cycle_pos)
                result = test_list.find_cycle_start()
                self.assertEqual(result, expected_data)

    def test_cycle_detection_larger_list(self):
        """Test cycle detection on larger list"""
        # Create list with 10 elements
        for i in range(1, 11):
            self.llist.append(i)

        # Create cycle: 10 -> 4 (position 3)
        self.llist.create_cycle(3)
        result = self.llist.find_cycle_start()
        self.assertEqual(result, 4)

    def test_cycle_detection_string_data(self):
        """Test cycle detection with string data"""
        words = ["apple", "banana", "cherry", "date"]
        for word in words:
            self.llist.append(word)

        # Create cycle: "date" -> "banana" (position 1)
        self.llist.create_cycle(1)
        result = self.llist.find_cycle_start()
        self.assertEqual(result, "banana")

    def test_cycle_detection_mixed_data_types(self):
        """Test cycle detection with mixed data types"""
        data = [1, "hello", 3.14, [1, 2], {"key": "value"}]
        for item in data:
            self.llist.append(item)

        # Create cycle: last element -> 3.14 (position 2)
        self.llist.create_cycle(2)
        result = self.llist.find_cycle_start()
        self.assertEqual(result, 3.14)

    def test_slow_fast_pointer_algorithm(self):
        """Test that the algorithm correctly implements Floyd's cycle detection"""
        # This test verifies the two-phase approach

        # Phase 1: Create a cycle and verify detection
        for i in range(1, 8):
            self.llist.append(i)

        # No cycle initially
        self.assertIsNone(self.llist.find_cycle_start())

        # Create cycle and verify detection
        self.llist.create_cycle(2)  # Points to element 3
        result = self.llist.find_cycle_start()
        self.assertEqual(result, 3)

    def test_edge_case_two_element_cycle(self):
        """Test cycle detection with two elements"""
        self.llist.append(1)
        self.llist.append(2)

        # Create cycle: 2 -> 1 (position 0)
        self.llist.create_cycle(0)
        result = self.llist.find_cycle_start()
        self.assertEqual(result, 1)

    def test_create_cycle_empty_list(self):
        """Test creating cycle on empty list"""
        self.llist.create_cycle(0)
        result = self.llist.find_cycle_start()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
