from exceptions import QueueEmptyError


class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0
    def add(self, value):
        """add value to end  (fifo)"""
        new_node = DoublyNode(value)
        if not self.tail:  # Empty queue
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._count += 1

    def pop(self):
        """get first value  (fifo)"""
        if not self.head:
            raise QueueEmptyError("Cannot pop.")
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._count -= 1
        return value

    def count(self):
        return self._count

    def clear(self):
        self.head = None
        self.tail = None
        self._count = 0

    def popAll(self):
        """ get [] of all elements """
        elements = []
        while self.head:
            elements.append(self.pop())
        return elements
