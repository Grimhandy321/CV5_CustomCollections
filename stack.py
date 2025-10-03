from exceptions import StackEmptyError


class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._count = 0

    def add(self, value):
        new_node = SinglyNode(value)
        new_node.next = self.top
        self.top = new_node
        self._count += 1

    def pop(self):
        if not self.top:
            raise StackEmptyError("Cannot pop.")
        value = self.top.value
        self.top = self.top.next
        self._count -= 1
        return value

    def count(self):
        return self._count

    def clear(self):
        self.top = None
        self._count = 0

    def popAll(self):
        elements = []
        while self.top:
            elements.append(self.pop())
        return elements
