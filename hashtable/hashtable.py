class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
        return self.head.value

    def find(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def delete(self, key):
        cur = self.head
        if cur.key == key:
            self.head = self.head.next
            return cur
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.key == key:  
                prev.next = cur.next  
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # size of internal array
        self.capacity = capacity
        # internal array (stores each inserted value in bucket based on provided key)
        self.data = [None] * self.capacity
        self.ll = [LinkedList()] * capacity
        self.elements = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.elements / self.capacity

# **********************************
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash
        

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # * Find the slot for the key
        slot = self.hash_index(key)
        # * Search the linked list for the key
        cur = self.ll[slot].find(key)
        # * If found, update it
        if cur is not None:
            cur.value = value 
            return cur.value
        # * If not found, make a new HashTableEntry and add it to the list
        else:
            return self.ll[slot].insert_at_head(HashTableEntry(key, value))

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # self.buckets[slot] = None
        # * Find the slot for the key
        slot = self.hash_index(key)
        # * Search the linked list for the key
        cur = self.ll[slot].find(key)
        # * If found, delete it from the linked list, then return the deleted value
        if cur is not None:
            return self.ll[slot].delete(key)

        # * If not found, return None
        else:
            return None
        # self.put(key, None)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Get Slot for Key
        # slot = self.hash_index(key)
        # # Store value there
        # hash_entry = self.data[slot]
        # if hash_entry is not None:
        #     return hash_entry.value

        # Find the slot for the key
        slot = self.hash_index(key)
        # * Search the linked list for the key
        cur = self.ll[slot].find(key)
        # * If found, return the value
        if cur is not None:
            return cur.value 
        # * If not found, return None
        else:
            return None 


# *************************************

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_table = self.data
        self.capacity = new_capacity
        self.data = [None] * self.capacity
        # if self.get_load_factor() > 0.7:
        #     new_table = [self.LinkedList()] * new_capacity
        for i in range(len(new_table)):
            current = new_table[i]
            while current is not None:
                self.put(current.key, current.value)
                current = current.next
                # slot = self.hash_index(key)
                # self.put(cur.key, cur.value)

                 # 1. Allocate a new array of bigger size, typically double the previous size (or half the size if resizing down, down to some minimum)
        # new_table = HashTable(new_capacity)
        # 2. Traverse the old hash table -- O(n) over the number of elements in the hash table

        # for i in range(len(new_data)):
        #     if new_data is not None:
        #         cur = new_data[i].head
        #         while cur.next is not None:
        #             # For each of the elements:
        #             #     Figure it's slot in the bigger (or smaller), new array
        #             #     Put it there
        #             self.put(cur.key, cur.value)
        #             cur = cur.next
        #         index = self.hash_index(cur.key)
        #         self.put(cur.key, cur.value)




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
