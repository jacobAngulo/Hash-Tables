

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


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


def hash(string, max):
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
    for i in range(len(storage)):
        if storage[i] == None:
            available_index = i
        elif storage[i][0] == key:
            available_index = i
            exists = True
    if exists:
        storage[i][1] = value
        print(f'warning: you have overwritten {key}')
    elif available_index == None:
        storage[len(storage)] = (key, value)
        print('warning: exceeds storage space')
    else:
        storage[available_index] = (key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    storage = hash_table.storage
    target_index = None
    for i in range(len(storage)):
        if storage[i] is not None:
            if storage[i][0] == key:
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
    for i in range(len(storage)):
        if storage[i] is not None:
            if storage[i][0] == key:
                target_index = i
    if target_index is not None:
        return storage[i][1]
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
