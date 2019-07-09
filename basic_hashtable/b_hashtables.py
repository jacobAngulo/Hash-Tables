

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, value):
        self.value = value
        self.right = None


class KeyBasedLinkedList:
    def __init__(self, key, root=None):
        self.key = key
        self.root = root

    def append(self, value):
        current = self.root
        while current.right is not None:
            current = current.right
        current.right = Pair(value)


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''


class BasicHashTable:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''


def hash(string):
    long_hash = 5381
    for char in string:
        long_hash = ((long_hash << 5) + long_hash) + ord(char)
    return long_hash


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    storage = hash_table.storage
    available_index = None
    exists = False
    key = hash(key)
    for i in range(len(storage)):
        if storage[i] == None:
            available_index = i
        elif storage[i].key == key:
            available_index = i
            exists = True
            break
    if exists:
        storage[available_index].append(value)
        print(f'warning: you have overwritten {key}')
    if available_index == None:
        storage[len(storage)] = KeyBasedLinkedList(key, Pair(value))
        print('warning: exceeds storage space')
    else:
        storage[available_index] = KeyBasedLinkedList(key, Pair(value))

    # '''
    # Fill this in.

    # If you try to remove a value that isn't there, print a warning.
    # '''


def hash_table_remove(hash_table, key):
    storage = hash_table.storage
    target_index = None
    key = hash(key)
    for i in range(len(storage)):
        if storage[i] is not None:
            if storage[i].key == key:
                target_index = i
    if target_index is not None:
        storage[target_index] = None
    else:
        print('warning: target does not exist')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    storage = hash_table.storage
    target_index = None
    key = hash(key)
    for i in range(len(storage)):
        if storage[i] is not None:
            if storage[i].key == key:
                target_index = i
    if target_index is not None:
        return storage[i].root.value
    else:
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
