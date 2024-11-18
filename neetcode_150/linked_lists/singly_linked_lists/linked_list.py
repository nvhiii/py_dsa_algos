from neetcode_150.linked_lists.singly_linked_lists.list_node import ListNode

class LinkedList:
    def __init__(self, val=None):
        if val is not None:
            self.head = ListNode(val) # initial node w val 4
            self.tail = self.head
        else:
            self.head = None
            self.tail = None
        # head and tail

    def insert(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # next pointer to new node
            self.tail = new_node

    def traverse(self):
        current = self.head
        while current:
            print(f"{current.value} -> ")
            current = current.next
        print("None")

    def insert_at_start(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node