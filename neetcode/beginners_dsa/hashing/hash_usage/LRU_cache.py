# intuition
# since we must track the least and most used key in the constraint of the size of the hm,
# we must implement this in constant time, access + put in o1
# need to keep track of linked list with head and tail pters
# need a node class

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        # need to impleemnt pointers, not just the vals
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # must have size via capacity init
        # implement a data structure to hold all the keys
        # hashmap
        self.cap = capacity
        self.cache = {}
        # update dll
        self.head, self.tail = Node(0,0), Node(0,0)
        # link them
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, key): # can be implemented via node
        # we are given a key val to the node in the hm, we remove it in the place in position the ll
        # we assume given a valid index
        n = self.cache[key]
        first = n.prev
        second = n.next
        first.next, second.prev = second, first

    def insert(self, key): # can be implemented via node
        # this method will insert the node at key to end of the linked list before tail dummy
        n = self.cache[key]
        first = self.tail.prev
        second = self.tail

        first.next = n
        n.prev = first
        n.next = second
        second.prev = n

    def get(self, key: int) -> int:
        # check if key in the hm, then update the pointer to mru (most recent used)
        # then return val to the key
        # else -1
        if key in self.cache:
            # must update
            # dont update update hashmap, just linked list
            self.remove(key) # remove it from where it is atm
            self.insert(key) # insert to the end, before dummy tail
            return self.cache[key].val # accessing cache[key] gives us the pointer to the node, not the inherent val
        return -1


    def put(self, key: int, value: int) -> None:
        # update val of key if it exists, basically need to update ptr
        # hm k = v
        # update hm based on constraint
        if key in self.cache:
            # update linked list here only
            self.remove(key)
        
        self.cache[key] = Node(key, value) # add the key to the cache if not exist
        self.insert(key) # no matter what, this will execute bc this will be the most recently executed

        # now we have a check after adding
        if len(self.cache) > self.cap:
            # remove LRU
            # access the lru
            lru = self.head.next # node we want
            self.remove(lru.key)
            del self.cache[lru.key] # each node has a key and val pair