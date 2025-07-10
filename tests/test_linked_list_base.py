import unittest
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.linked_list_base import Node, LinkedList


class TestNode(unittest.TestCase):
    def test_node_creation(self):
        """Test Node creation with data"""
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.next)

    def test_node_linking(self):
        """Test linking nodes together"""
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2

        self.assertEqual(node1.data, 1)
        self.assertEqual(node1.next.data, 2)
        self.assertIsNone(node2.next)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.llist = LinkedList()

    def test_empty_list_creation(self):
        """Test creating an empty linked list"""
        self.assertIsNone(self.llist.head)

    def test_append_single_element(self):
        """Test appending a single element to empty list"""
        self.llist.append(1)
        self.assertIsNotNone(self.llist.head)
        self.assertEqual(self.llist.head.data, 1)
        self.assertIsNone(self.llist.head.next)

    def test_append_multiple_elements(self):
        """Test appending multiple elements"""
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.llist.append(element)

        # Verify the list structure
        current = self.llist.head
        for expected in elements:
            self.assertIsNotNone(current)
            self.assertEqual(current.data, expected)
            current = current.next

        # Verify the last node points to None
        self.assertIsNone(current)

    def test_append_different_data_types(self):
        """Test appending different data types"""
        self.llist.append(1)
        self.llist.append("hello")
        self.llist.append(3.14)
        self.llist.append([1, 2, 3])

        current = self.llist.head
        self.assertEqual(current.data, 1)
        current = current.next
        self.assertEqual(current.data, "hello")
        current = current.next
        self.assertEqual(current.data, 3.14)
        current = current.next
        self.assertEqual(current.data, [1, 2, 3])

    def test_print_list_empty(self):
        """Test printing an empty list"""
        captured_output = StringIO()
        sys.stdout = captured_output

        self.llist.print_list()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "None")

    def test_print_list_single_element(self):
        """Test printing a list with single element"""
        self.llist.append(42)

        captured_output = StringIO()
        sys.stdout = captured_output

        self.llist.print_list()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "42 -> None")

    def test_print_list_multiple_elements(self):
        """Test printing a list with multiple elements"""
        for i in range(1, 6):
            self.llist.append(i)

        captured_output = StringIO()
        sys.stdout = captured_output

        self.llist.print_list()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1 -> 2 -> 3 -> 4 -> 5 -> None")


if __name__ == '__main__':
    unittest.main()
