# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'<{self.key}, {self.value}'


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0  # number of elements that have been inserted

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.

        Python HASH function

        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.

        This
        '''
        self.size += 1  # increment size
        # Hashmod the key to find the bucket
        index = self._hash_mod(key)  # Compute index of key
        # Check if a pair already exisit in the bucket
        pair = self.storage[index]  # Go to the node corresponding to the hash

        # if bucket is empty
        if pair is None:
            # create pair, add it return
            self.storage[index] = LinkedPair(key, value)
            return
            # collision iterate to the end of the linked list at provided index
        prev = pair
        while pair is not None:
            prev = pair
            pair = pair.next

        # Add a new pair at the end of the list with provided key/value
        prev.next = LinkedPair(key, value)

        #    # If bucket is empty, overwrite the key/value and throw a warning
        #    if pair.key != key:
        #        print("Warning: Overwriting value")
        #        pair.key = key
        #    pair.value = value
        # else:
        #    # If bucket is not empty, create a LinkedPair and place it in the bucket
        #    self.storage[index] = LinkedPair(key, value)

        # array_index = self._hash_mod(self._hash(key))
        # self.storage[array_index] = value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.

        THIS
        '''
        # index = self._hash_mod(key)  # Compute index of key
        # pair = self.storage[index]
        # prev = None

        # while pair is not None and pair.key != key:
        #    prev = pair
        #    pair = pair.next

        # if pair is None:
        #    return None

        # else:
        #    self.size -= 1
        #    result = pair.value
        #    if prev is None:
        #        pair = None
        #    else:
        #        prev.next = prev.next.next

        #    return result

        index = self._hash_mod(key)  # Compute index of key
        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # If so, remove that pair
            self.storage[index] = None
        else:
            # Else print warning
            print("Warning: Key does not exist")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        THIS
        '''
        # Get the index from hashmod
        index = self._hash_mod(key)

        pair = self.storage[index]

        while pair is not None and pair.key != key:
            pair = pair.next

        if pair is None:
            # Not found
            return None

        else:
            return pair.value  # found: return the data value

        # Get the index from hashmod
        # index = self._hash_mod(key)
        # Check if a pair exists in the bucket with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #    # If so, return the value
        #    return self.storage[index].value
        # else:
        #    # Else return None
        #    return None

        # array_index = self._hash_mod(self._hash(key))
        # return self.storage[array_index]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        AND THIS
        '''
        old_storage = self.storage
        self.capacity *= 2

        # create a new array size * 2
        self.storage = [None] * self.capacity

        # move all values over
        for pair in old_storage:
            # re-insert each key/value
            self.insert(pair.key, pair.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
