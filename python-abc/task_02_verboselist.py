#!/usr/bin/env python3

class VerboseList(list):
    """
    A list subclass that prints notification messages when items are added or removed.
    Overrides append, extend, remove, and pop methods to add verbosity.
    """
    
    def append(self, item):
        """
        Add an item to the end of the list and print a notification.
        
        Args:
            item: The item to be added to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """
        Extend the list with an iterable and print a notification.
        
        Args:
            iterable: The iterable whose items will be added to the list
        """
        # Convert to list first to get the count
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")
    
    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print a notification.
        
        Args:
            item: The item to be removed
        """
        # Check if the item exists before attempting to remove
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Cannot remove [{item}]: item not in list.")
    
    def pop(self, index=-1):
        """
        Remove and return an item at the given index and print a notification.
        If no index is specified, removes and returns the last item.
        
        Args:
            index: The index of the item to be removed (default: -1, the last item)
            
        Returns:
            The removed item
        """
        try:
            item = self[index]  # Get the item before removing
            print(f"Popped [{item}] from the list.")
            return super().pop(index)
        except IndexError:
            print("Cannot pop: list is empty or index out of range.")
            raise  # Re-raise the exception
