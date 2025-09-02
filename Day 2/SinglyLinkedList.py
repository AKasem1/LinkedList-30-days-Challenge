#https://neetcode.io/problems/singlyLinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        current = self.head
        for _ in range (index):
            current = current.next
        return current.data

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            # removed_data = self.head.data
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return True
        current = self.head
        for _ in range (index - 1):
            current = current.next
        to_remove = current.next
        current.next = to_remove.next

        if index == self.size - 1:
            self.tail = current
            
        self.size -= 1
        return True

    def getValues(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values
        
