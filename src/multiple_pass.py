from typing import Optional, Any
from .linked_list_base import LinkedList


class MultiplePassLinkedList(LinkedList):
    """A linked list that implements the multiple-pass technique.
    
    This class demonstrates the multiple-pass technique for finding the middle
    element of a linked list. It uses two passes: first to count nodes, then
    to traverse to the middle position.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    def find_middle(self) -> Optional[Any]:
        """Find the middle element using the multiple-pass technique.
        
        This method makes two passes through the list:
        1. First pass: Count the total number of nodes
        2. Second pass: Traverse to the middle position
        
        For even-length lists, returns the first middle element.
        For example, in a list [1, 2, 3, 4], returns 2.
        
        Returns:
            The data of the middle node, or None if the list is empty
            
        Example:
            >>> llist = MultiplePassLinkedList()
            >>> for i in range(1, 6):
            ...     llist.append(i)
            >>> llist.find_middle()
            3
        """
        if not self.head:
            return None

        # First Pass: Count the total number of nodes
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        # Second Pass: Traverse to the middle node
        middle_position = count // 2
        current = self.head
        for _ in range(middle_position):
            current = current.next

        return current.data

# Example usage
if __name__ == "__main__":
    # Quick validation of functionality
    llist = MultiplePassLinkedList()
    
    # Test with odd length
    for i in range(1, 6):
        llist.append(i)
    print(f"List: {llist}")
    print(f"Length: {len(llist)}, Middle: {llist.find_middle()}")
    
    # Test with even length
    llist.append(6)
    print(f"List: {llist}")
    print(f"Length: {len(llist)}, Middle: {llist.find_middle()}")
    
    # Test edge cases
    empty_list = MultiplePassLinkedList()
    print(f"Empty list middle: {empty_list.find_middle()}")
    
    single_list = MultiplePassLinkedList()
    single_list.append(42)
    print(f"Single element middle: {single_list.find_middle()}")
