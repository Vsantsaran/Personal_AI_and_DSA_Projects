# Stack implementation using SLL

class LinkedList:
    class _Node:
        def __init__(self, val, _node):
            self._data = val
            self._next = _node

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def push(self, val):
        self._size += 1
        self._head = LinkedList._Node(val, self._head)

    def pop(self):
        if not self.is_empty():
            self._size -= 1
            temp_node = self._head
            self._head = self._head._next
            return temp_node._data
        else:
            return 'Stack is empty.'

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


stk = LinkedList()
for i in range(10):
    stk.push(i)
print(stk)
