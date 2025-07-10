from typing import Optional, Any
from .linked_list_base import LinkedList, Node


class TemporaryHeadLinkedList(LinkedList):
    """A linked list that implements the temporary head technique.
    
    This class demonstrates the temporary head (dummy node) technique for
    simplifying deletion and reversal operations. The temporary head helps
    handle edge cases uniformly, especially when the head node needs to be
    modified.
    
    Time Complexity: O(n) for both delete and reverse operations
    Space Complexity: O(1)
    """
    
    def delete_node(self, value: Any) -> bool:
        """Delete the first occurrence of a node with the given value.
        
        This method uses the temporary head technique to simplify deletion,
        especially when deleting the head node. A dummy node is created to
        act as a temporary head, making the deletion logic uniform for all positions.
        
        Args:
            value: The value to search for and delete
            
        Returns:
            True if the node was found and deleted, False otherwise
            
        Example:
            >>> llist = TemporaryHeadLinkedList()
            >>> for i in range(1, 6):
            ...     llist.append(i)
            >>> llist.delete_node(3)  # Delete middle node
            True
            >>> llist.delete_node(1)  # Delete head node
            True
        """
        dummy = Node(0)  # Create temporary head node
        dummy.next = self.head
        prev, current = dummy, self.head
        
        while current:
            if current.data == value:
                prev.next = current.next
                self.head = dummy.next  # Update in case head was deleted
                return True
            prev, current = current, current.next
            
        self.head = dummy.next  # Update head (though it shouldn't have changed)
        return False

    def reverse(self) -> None:
        """Reverse the linked list using the temporary head technique.
        
        This method uses a temporary head node to simplify the reversal process.
        The dummy node helps maintain a consistent reference point during the
        reversal operation.
        
        The algorithm works by:
        1. Creating a temporary head node
        2. Reversing the links between nodes
        3. Updating the actual head to point to the new first node
        4. Fixing the old head's next pointer
        
        Example:
            >>> llist = TemporaryHeadLinkedList()
            >>> for i in range(1, 4):
            ...     llist.append(i)
            >>> print(llist)  # 1 -> 2 -> 3 -> None
            >>> llist.reverse()
            >>> print(llist)  # 3 -> 2 -> 1 -> None
        """
        # Handle empty list case
        if not self.head:
            return

        # Create a temporary head node pointing to the actual head
        temp_head = Node(0)  # Dummy node with arbitrary value
        temp_head.next = self.head

        prev = temp_head
        current = self.head

        # Reverse the list
        while current:
            # Store next node
            next_node = current.next
            # Reverse the link
            current.next = prev
            # Move prev and current one step forward
            prev = current
            current = next_node

        # Update the actual head
        # prev is the new head, temp_head.next is the old head
        self.head = prev
        # Fix the old head's next pointer (which points to temp_head)
        if temp_head.next:
            temp_head.next.next = None

# Example usage
if __name__ == "__main__":
    # Quick validation of functionality
    llist = TemporaryHeadLinkedList()
    
    # Test deletion
    for i in range(1, 6):
        llist.append(i)
    print(f"Original: {llist}")
    
    result = llist.delete_node(3)
    print(f"Delete 3: {result}, List: {llist}")
    
    result = llist.delete_node(1)  # Delete head
    print(f"Delete head: {result}, List: {llist}")
    
    result = llist.delete_node(99)  # Non-existent
    print(f"Delete non-existent: {result}, List: {llist}")
    
    # Test reversal
    print(f"Before reverse: {llist}")
    llist.reverse()
    print(f"After reverse: {llist}")
    
    # Test edge cases
    empty_list = TemporaryHeadLinkedList()
    empty_list.reverse()
    print(f"Empty list reverse: {empty_list}")
