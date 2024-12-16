# disclaimer: this wont pass the testcases, but it is a good learning idea
class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        # size, capacity, and map init
        self.size = 0 # no items
        self.capacity = capacity # provided a constructor param, but usually do smallest prime like 2
        self.map = [None] * self.capacity # none initialized map

    # very noob implementation of a hashing function
    def hash(self, key):
        index = 0
        for c in key: # we assume key is a string
            index += ord(c)
        return index % self.capacity # we mod capacity, so we do not get index out of bounds error

    def insert(self, key: int, value: int) -> None:
        # no checks needed
        index = self.hash(key)
        while True:
            if self.map[index] == None: # doesnt exist
                self.map[index] = value
                self.size += 1
                if self.size >= self.capacity // 2: # ratio greater than 0.5 (can be range of 0.5 to 0.7)
                    self.resize() # usually a rehash function, but in this case we named it resize
                return
            else: # exists, just update val of the given key
                self.map[index] = value

            index += 1
            index = index % self.capacity # open addressing

    def get(self, key: int) -> int:
        # no checks
        index = self.hash(key)
        while self.map[key] != None:
            if self.map[key].key == key:
                return self.map[key].val
            # open address
            index += 1
            index = index % self.capacity
        return None # not found

    def remove(self, key: int) -> bool:
        # check
        if not self.get(key):
            return None

        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index += 1
            index = index % self.capacity
        return False # not found

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new = []
        for i in range(self.capacity):
            new.append(None)

        old = self.map
        self.map = new
        for pair in old:
            if pair:
                self.insert(pair.key, pair.val)
