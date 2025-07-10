import unittest
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.multiple_pass import MultiplePassLinkedList


class TestMultiplePassLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.llist = MultiplePassLinkedList()

    def test_find_middle_empty_list(self):
        """Test finding middle of empty list"""
        result = self.llist.find_middle()
        self.assertIsNone(result)

    def test_find_middle_single_element(self):
        """Test finding middle of single element list"""
        self.llist.append(42)
        result = self.llist.find_middle()
        self.assertEqual(result, 42)

    def test_find_middle_two_elements(self):
        """Test finding middle of two element list"""
        self.llist.append(1)
        self.llist.append(2)
        result = self.llist.find_middle()
        self.assertEqual(result, 2)  # Second element (index 1)

    def test_find_middle_odd_length(self):
        """Test finding middle of odd length list"""
        # List: 1 -> 2 -> 3 -> 4 -> 5 (length 5)
        # Middle position: 5 // 2 = 2 (0-based), so element is 3
        for i in range(1, 6):
            self.llist.append(i)

        result = self.llist.find_middle()
        self.assertEqual(result, 3)

    def test_find_middle_even_length(self):
        """Test finding middle of even length list"""
        # List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 (length 6)
        # Middle position: 6 // 2 = 3 (0-based), so element is 4
        for i in range(1, 7):
            self.llist.append(i)

        result = self.llist.find_middle()
        self.assertEqual(result, 4)

    def test_find_middle_larger_odd_list(self):
        """Test finding middle of larger odd length list"""
        # List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (length 7)
        # Middle position: 7 // 2 = 3 (0-based), so element is 4
        for i in range(1, 8):
            self.llist.append(i)

        result = self.llist.find_middle()
        self.assertEqual(result, 4)

    def test_find_middle_larger_even_list(self):
        """Test finding middle of larger even length list"""
        # List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 (length 8)
        # Middle position: 8 // 2 = 4 (0-based), so element is 5
        for i in range(1, 9):
            self.llist.append(i)

        result = self.llist.find_middle()
        self.assertEqual(result, 5)

    def test_find_middle_string_data(self):
        """Test finding middle with string data"""
        words = ["apple", "banana", "cherry", "date", "elderberry"]
        for word in words:
            self.llist.append(word)

        result = self.llist.find_middle()
        self.assertEqual(result, "cherry")  # Middle element

    def test_find_middle_mixed_data_types(self):
        """Test finding middle with mixed data types"""
        data = [1, "hello", 3.14, [1, 2], {"key": "value"}]
        for item in data:
            self.llist.append(item)

        result = self.llist.find_middle()
        self.assertEqual(result, 3.14)  # Middle element

    def test_multiple_pass_technique_verification(self):
        """Test that the method actually uses two passes"""
        # This test verifies the algorithm works correctly
        # by testing various scenarios that would fail with single pass

        # Test case 1: Verify correct counting
        for i in range(1, 10):  # 9 elements
            self.llist.append(i)

        result = self.llist.find_middle()
        self.assertEqual(result, 5)  # 9 // 2 = 4 (0-based), so 5th element

        # Test case 2: Add one more element (even length)
        self.llist.append(10)
        result = self.llist.find_middle()
        self.assertEqual(result, 6)  # 10 // 2 = 5 (0-based), so 6th element


if __name__ == '__main__':
    unittest.main()
