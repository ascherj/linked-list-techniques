from typing import Optional, Any
from .linked_list_base import LinkedList


class SlowFastLinkedList(LinkedList):
    """A linked list that implements the slow-fast pointer technique.
    
    This class demonstrates Floyd's cycle detection algorithm (also known as the
    "tortoise and hare" algorithm) for detecting cycles in linked lists and
    finding the start of the cycle.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    def create_cycle(self, pos: int) -> bool:
        """Create a cycle by connecting the last node to the node at given position.
        
        This method is used for testing cycle detection. It connects the last node
        of the list to the node at the specified position (0-based indexing).
        
        Args:
            pos: The 0-based position where the cycle should start.
                 Must be non-negative and less than the list length.
                 
        Returns:
            True if the cycle was created successfully, False otherwise.
            
        Example:
            >>> llist = SlowFastLinkedList()
            >>> for i in range(1, 6):  # Creates 1 -> 2 -> 3 -> 4 -> 5
            ...     llist.append(i)
            >>> llist.create_cycle(1)  # Creates cycle: 5 -> 2
            True
        """
        if pos < 0:
            return False
            
        cycle_node = None
        current = self.head
        count = 0
        last = None

        # Find the node at position and last node
        while current:
            if count == pos:
                cycle_node = current
            last = current
            current = current.next
            count += 1

        # Connect last node to cycle_node
        if last and cycle_node:
            last.next = cycle_node
            return True
        return False

    def find_cycle_start(self) -> Optional[Any]:
        """Find the start of a cycle using Floyd's cycle detection algorithm.
        
        This method implements the slow-fast pointer technique (Floyd's algorithm)
        to detect if there's a cycle in the linked list and find where it starts.
        
        The algorithm works in two phases:
        1. Detection: Use slow (1 step) and fast (2 steps) pointers to detect a cycle
        2. Finding start: Reset slow to head, move both at same speed until they meet
        
        Returns:
            The data of the node where the cycle starts, or None if no cycle exists.
            
        Example:
            >>> llist = SlowFastLinkedList()
            >>> for i in range(1, 6):
            ...     llist.append(i)
            >>> llist.create_cycle(1)  # Cycle starts at position 1 (value 2)
            >>> llist.find_cycle_start()
            2
        """
        if not self.head or not self.head.next:
            return None

        # Phase 1: Detect cycle using slow and fast pointers
        slow = self.head
        fast = self.head

        # Move slow by 1, fast by 2 until they meet or reach end
        while fast and fast.next:
            slow = slow.next           # Moves one step
            fast = fast.next.next      # Moves two steps
            if slow == fast:          # Cycle detected
                break
        else:
            return None  # No cycle if fast reaches end

        # Phase 2: Find cycle start
        # Reset slow to head, move both at same speed until they meet
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data  # Return data at cycle start

# Example usage
if __name__ == "__main__":
    # Quick validation of functionality
    llist = SlowFastLinkedList()
    
    # Test without cycle
    for i in range(1, 6):
        llist.append(i)
    print(f"List: {llist}")
    print(f"Cycle detected: {llist.find_cycle_start() is not None}")
    
    # Test with cycle
    llist.create_cycle(1)  # Creates cycle: 5 -> 2
    cycle_start = llist.find_cycle_start()
    print(f"After creating cycle at position 1: {cycle_start}")
    
    # Test edge cases
    empty_list = SlowFastLinkedList()
    print(f"Empty list cycle: {empty_list.find_cycle_start()}")
    
    single_list = SlowFastLinkedList()
    single_list.append(42)
    print(f"Single element cycle: {single_list.find_cycle_start()}")
