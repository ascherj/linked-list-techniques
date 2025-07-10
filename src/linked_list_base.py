from typing import Optional, Any


class Node:
    """A node in a linked list.
    
    Attributes:
        data: The data stored in the node
        next: Reference to the next node, or None if this is the last node
    """
    
    def __init__(self, data: Any) -> None:
        """Initialize a new node.
        
        Args:
            data: The data to store in this node
        """
        self.data = data
        self.next: Optional['Node'] = None


class LinkedList:
    """A singly linked list implementation.
    
    This is the base class for all linked list implementations in this package.
    Provides basic operations like append, print, length, and string representation.
    
    Attributes:
        head: Reference to the first node, or None if the list is empty
    """
    
    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        """Add a new node with the given data to the end of the list.
        
        Args:
            data: The data to store in the new node
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self) -> None:
        """Print the list in a readable format (data -> data -> ... -> None)."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def __len__(self) -> int:
        """Return the number of nodes in the list.
        
        Returns:
            The count of nodes in the list
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def __str__(self) -> str:
        """Return a string representation of the list.
        
        Returns:
            A string in the format "data -> data -> ... -> None"
        """
        if not self.head:
            return "None"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        result.append("None")
        return " -> ".join(result)
