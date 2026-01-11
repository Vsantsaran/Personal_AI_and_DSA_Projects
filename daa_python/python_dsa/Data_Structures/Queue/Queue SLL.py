# Queue implementation using SLL

class LinkedList:
    class _Node:
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

    def dequeue(self):
        self._size -= 1
        if self.is_empty():
            return 'Queue is empty.'
        temp = self._head
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        return temp._data

    def peek(self):
        return self._head._data

    def is_empty(self):
        return self._head is None

    def __str__(self):
        temp = self._head
        llist = []
        while temp:
            llist.append(temp._data)
            temp = temp._next
        return str(llist)


qu = LinkedList()
for i in range(10):
    qu.enqueue(i)
qu.dequeue()
qu.dequeue()
qu.enqueue(100)
print(qu.peek())
print(qu)
