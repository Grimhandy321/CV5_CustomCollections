import unittest
from myqueue import Queue
from stack import Stack
from exceptions import QueueEmptyError, StackEmptyError


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_add_and_count(self):
        self.q.add(1)
        self.q.add(2)
        self.assertEqual(self.q.count(), 2)

    def test_pop(self):
        self.q.add(10)
        self.q.add(20)
        self.assertEqual(self.q.pop(), 10)  # FIFO
        self.assertEqual(self.q.pop(), 20)

    def test_pop_empty_raises(self):
        with self.assertRaises(QueueEmptyError):
            self.q.pop()

    def test_clear(self):
        self.q.add(1)
        self.q.add(2)
        self.q.clear()
        self.assertEqual(self.q.count(), 0)
        with self.assertRaises(QueueEmptyError):
            self.q.pop()

    def test_popAll(self):
        self.q.add("a")
        self.q.add("b")
        self.q.add("c")
        result = self.q.popAll()
        self.assertEqual(result, ["a", "b", "c"])
        self.assertEqual(self.q.count(), 0)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_add_and_count(self):
        self.s.add(1)
        self.s.add(2)
        self.assertEqual(self.s.count(), 2)

    def test_pop(self):
        self.s.add("x")
        self.s.add("y")
        self.assertEqual(self.s.pop(), "y")  # LIFO
        self.assertEqual(self.s.pop(), "x")

    def test_pop_empty_raises(self):
        with self.assertRaises(StackEmptyError):
            self.s.pop()

    def test_clear(self):
        self.s.add("a")
        self.s.add("b")
        self.s.clear()
        self.assertEqual(self.s.count(), 0)
        with self.assertRaises(StackEmptyError):
            self.s.pop()

    def test_popAll(self):
        self.s.add(1)
        self.s.add(2)
        self.s.add(3)
        result = self.s.popAll()
        self.assertEqual(result, [3, 2, 1])  # LIFO order
        self.assertEqual(self.s.count(), 0)


if __name__ == "__main__":
    unittest.main()
