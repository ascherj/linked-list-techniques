"""
Linked List Implementations Package

This package contains various linked list implementations demonstrating
different algorithmic techniques:

- LinkedList: Base linked list implementation
- MultiplePassLinkedList: Demonstrates multiple pass technique
- SlowFastLinkedList: Demonstrates slow-fast pointer technique
- TemporaryHeadLinkedList: Demonstrates temporary head technique
"""

from .linked_list_base import Node, LinkedList
from .multiple_pass import MultiplePassLinkedList
from .slow_fast import SlowFastLinkedList
from .temporary_head import TemporaryHeadLinkedList

__all__ = [
    'Node',
    'LinkedList',
    'MultiplePassLinkedList',
    'SlowFastLinkedList',
    'TemporaryHeadLinkedList'
]

__version__ = '1.0.0'
__author__ = 'TIP102 Student'
