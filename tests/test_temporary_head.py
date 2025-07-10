import unittest
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.temporary_head import TemporaryHeadLinkedList


class TestTemporaryHeadLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.llist = TemporaryHeadLinkedList()

    def _get_list_as_array(self):
        """Helper method to convert linked list to array for easy testing"""
        result = []
        current = self.llist.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    # Tests for delete_node method
    def test_delete_node_empty_list(self):
        """Test deleting from empty list"""
        self.llist.delete_node(1)
        self.assertIsNone(self.llist.head)

    def test_delete_node_single_element_found(self):
        """Test deleting the only element in list"""
        self.llist.append(42)
        self.llist.delete_node(42)
        self.assertIsNone(self.llist.head)

    def test_delete_node_single_element_not_found(self):
        """Test deleting non-existent element from single element list"""
        self.llist.append(42)
        self.llist.delete_node(99)
        self.assertEqual(self.llist.head.data, 42)
        self.assertIsNone(self.llist.head.next)

    def test_delete_node_head_element(self):
        """Test deleting head element from multi-element list"""
        for i in range(1, 6):
            self.llist.append(i)

        self.llist.delete_node(1)
        result = self._get_list_as_array()
        self.assertEqual(result, [2, 3, 4, 5])

    def test_delete_node_middle_element(self):
        """Test deleting middle element"""
        for i in range(1, 6):
            self.llist.append(i)

        self.llist.delete_node(3)
        result = self._get_list_as_array()
        self.assertEqual(result, [1, 2, 4, 5])

    def test_delete_node_tail_element(self):
        """Test deleting tail element"""
        for i in range(1, 6):
            self.llist.append(i)

        self.llist.delete_node(5)
        result = self._get_list_as_array()
        self.assertEqual(result, [1, 2, 3, 4])

    def test_delete_node_not_found(self):
        """Test deleting non-existent element"""
        for i in range(1, 6):
            self.llist.append(i)

        original = self._get_list_as_array()
        self.llist.delete_node(99)
        result = self._get_list_as_array()
        self.assertEqual(result, original)

    def test_delete_node_multiple_deletions(self):
        """Test multiple deletions"""
        for i in range(1, 6):
            self.llist.append(i)

        self.llist.delete_node(2)
        self.llist.delete_node(4)
        result = self._get_list_as_array()
        self.assertEqual(result, [1, 3, 5])

    def test_delete_node_string_data(self):
        """Test deleting with string data"""
        words = ["apple", "banana", "cherry", "date"]
        for word in words:
            self.llist.append(word)

        self.llist.delete_node("banana")
        result = self._get_list_as_array()
        self.assertEqual(result, ["apple", "cherry", "date"])

    # Tests for reverse method
    def test_reverse_empty_list(self):
        """Test reversing empty list"""
        self.llist.reverse()
        self.assertIsNone(self.llist.head)

    def test_reverse_single_element(self):
        """Test reversing single element list"""
        self.llist.append(42)
        self.llist.reverse()
        self.assertEqual(self.llist.head.data, 42)
        self.assertIsNone(self.llist.head.next)

    def test_reverse_two_elements(self):
        """Test reversing two element list"""
        self.llist.append(1)
        self.llist.append(2)

        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, [2, 1])

    def test_reverse_multiple_elements(self):
        """Test reversing multiple element list"""
        for i in range(1, 6):
            self.llist.append(i)

        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_reverse_string_data(self):
        """Test reversing with string data"""
        words = ["apple", "banana", "cherry"]
        for word in words:
            self.llist.append(word)

        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, ["cherry", "banana", "apple"])

    def test_reverse_twice(self):
        """Test reversing twice returns to original"""
        original = [1, 2, 3, 4, 5]
        for i in original:
            self.llist.append(i)

        self.llist.reverse()
        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, original)

    def test_reverse_large_list(self):
        """Test reversing larger list"""
        original = list(range(1, 11))  # [1, 2, 3, ..., 10]
        for i in original:
            self.llist.append(i)

        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, original[::-1])  # [10, 9, 8, ..., 1]

    # Combined tests
    def test_delete_then_reverse(self):
        """Test deleting elements then reversing"""
        for i in range(1, 6):
            self.llist.append(i)

        self.llist.delete_node(3)  # Remove middle element
        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, [5, 4, 2, 1])

    def test_reverse_then_delete(self):
        """Test reversing then deleting elements"""
        for i in range(1, 6):
            self.llist.append(i)

        self.llist.reverse()  # [5, 4, 3, 2, 1]
        self.llist.delete_node(3)  # Remove middle element
        result = self._get_list_as_array()
        self.assertEqual(result, [5, 4, 2, 1])

    def test_temporary_head_technique_verification(self):
        """Test that methods properly use temporary head technique"""
        # This test verifies edge cases that temporary head technique handles well

        # Test deleting head multiple times
        for i in range(1, 6):
            self.llist.append(i)

        # Delete head elements consecutively
        self.llist.delete_node(1)
        self.llist.delete_node(2)
        self.llist.delete_node(3)

        result = self._get_list_as_array()
        self.assertEqual(result, [4, 5])

        # Test reverse still works
        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, [5, 4])

    def test_mixed_data_types(self):
        """Test with mixed data types"""
        data = [1, "hello", 3.14, [1, 2]]
        for item in data:
            self.llist.append(item)

        self.llist.delete_node("hello")
        self.llist.reverse()
        result = self._get_list_as_array()
        self.assertEqual(result, [[1, 2], 3.14, 1])


if __name__ == '__main__':
    unittest.main()
