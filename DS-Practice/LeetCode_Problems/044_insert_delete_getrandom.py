'''
mplement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

'''

from random import choice

class RandomizedSet:
    def __init__(self):
        """Initialize the data structure."""
        # Dictionary to store value -> index mapping
        self.val_to_index = {}
        # List to store actual values for O(1) random access
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Insert a value to the set. Returns true if the set did not already contain the specified element.
      
        Args:
            val: The value to insert
          
        Returns:
            True if insertion was successful, False if value already exists
        """
        # Check if value already exists
        if val in self.val_to_index:
            return False
      
        # Add value to the end of the list
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Remove a value from the set. Returns true if the set contained the specified element.
      
        Args:
            val: The value to remove
          
        Returns:
            True if removal was successful, False if value doesn't exist
        """
        # Check if value exists
        if val not in self.val_to_index:
            return False
      
        # Get index of element to remove
        index_to_remove = self.val_to_index[val]
        last_element = self.values[-1]
      
        # Move the last element to the position of element to remove
        self.values[index_to_remove] = last_element
        self.val_to_index[last_element] = index_to_remove
      
        # Remove the last element from list and the value from dictionary
        self.values.pop()
        del self.val_to_index[val]
      
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
      
        Returns:
            A random value from the set
        """
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


'''
Below solution does not provide O(1) for getRandom.

import random

class RandomizedSet:

    def __init__(self):
        self.randomizedSet = set()
        
    def insert(self, val: int) -> bool:
        if self.randomizedSet[val]:
            return false

        self.randomizedSet.add(val)
        return true

    def remove(self, val: int) -> bool:
        if self.randomizedSet[val]:
            self.randomizedSet.remove(val)
            return true
        return false

    def getRandom(self) -> int:
        return random.choice(tuple(self.randomizedSet))

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
