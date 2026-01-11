# Circular Queue implementation using SLL

class CircularQueue:
    __slots__ = '_head', '_tail', '_size'
    class _Node:
        __slots__ = '_data', '_next'
        def __init__(self, val):
            self._data = val
            self._next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, val):
        self._size += 1
        _node = self._Node(val)
        if self.is_empty():
            self._head = _node
        else:
            self._tail._next = _node
        self._tail = _node
        self._tail._next = self._head

    def dequeue(self):
        self._size -= 1
        if self.is_empty():
            return 'Queue is empty.'
        temp = self._head
        self._tail._next = temp._next
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        return temp._data

    def rotate(self, _n):
        _n = abs(self._size - _n)
        for i in range(_n):
            self._tail = self._head
            self._head = self._head._next


    def peek(self):
        return self._head._data

    def is_empty(self):
        return self._head is None

    def __str__(self):
        temp = self._head
        llist = []
        while temp is not self._tail:
            llist.append(temp._data)
            temp = temp._next
        llist.append(self._tail._data)
        return str(llist)


cq = CircularQueue()
cq.enqueue(12)
cq.enqueue(3)
cq.enqueue(2)
cq.enqueue(33)
cq.enqueue(54)
cq.enqueue(60)
cq.enqueue(-3)
print(cq)
cq.dequeue()
print(cq)
cq.rotate(-4)
print(cq)
