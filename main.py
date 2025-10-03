from myqueue import Queue
from stack import Stack
from exceptions import QueueEmptyError, StackEmptyError


if __name__ == "__main__":
    print("Queue:")
    q = Queue()
    q.add(10)
    q.add(20)
    q.add(30)
    print("Queue count:", q.count())  # 3
    print("Queue pop:", q.pop())      # 10
    print("Queue popAll:", q.popAll()) # [20, 30]
    print("Queue count after popAll:", q.count())  # 0

    print("\nStack:")
    s = Stack()
    s.add("A")
    s.add("B")
    s.add("C")
    print("Stack count:", s.count())  # 3
    print("Stack pop:", s.pop())      # C
    print("Stack popAll:", s.popAll()) # ['B', 'A']
    print("Stack count after popAll:", s.count())  # 0
    try:
        q.pop()
    except QueueEmptyError as e:
        print("Queue error:", e)

    try:
        s.pop()
    except StackEmptyError as e:
        print("Stack error:", e)
