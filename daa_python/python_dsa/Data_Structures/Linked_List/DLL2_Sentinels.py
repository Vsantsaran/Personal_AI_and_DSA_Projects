# DLL with two sentinels (dummy nodes at both ends)

class Node:
    __slots__ = '_data', '_next', '_prev', '_id'
    _start_id = -2

    def __init__(self, val=None):
        self._data = val
        self._id = Node._start_id + 1
        self._next = self._prev = None
        Node._start_id += 1


class DLL:
    __slots__ = '_head', '_size', '_header', '_trailer'

    def __init__(self):
        self._head = self._header = Node()
        self._trailer = Node()
        self._head._next = self._header._next = self._trailer
        self._trailer._prev = self._header = self._head
        self._size = 0

    def insert(self, pos, val):
        if pos < 1 or pos > self._size+1:
            print('Invalid position.')
            return
        if not val:
            return print('0 cannot be inserted.')
        self._size += 1
        _node = Node(val)
        temp = self._head
        for _ in range(pos-1):
            temp = temp._next
        _node._prev = temp
        _node._next = temp._next
        _node._next._prev = temp._next = _node

    def delete(self, pos):
        if pos < 1 or pos > self._size:
            print('Invalid position.')
            return
        self._size -= 1
        temp = self._head
        for _ in range(pos-1):
            temp = temp._next
        del_node = temp._next
        temp._next = del_node._next
        dat = del_node._data
        del del_node
        return dat

    def sort(self):
        for i in range(1, self._size):
            smallest_pos = self._smallest_node(i)
            dat = self.delete(smallest_pos)
            self.insert(i, dat)

    def _smallest_node(self, start):
        temp = self._head._next
        for j in range(1, start):
            temp = temp._next
        s = temp._data
        index = start
        for i in range(start, self._size):
            if s > temp._next._data:
                s = temp._next._data
                index = i + 1
            temp = temp._next
        return index

    def search(self, sval):
        '''this func searches for a value'''
        temp = self._head._next
        while temp:
            if temp._data == sval:
                return 'Yes'
            temp = temp._next
        return 'No'

    def __len__(self):
        return self._size

    def __del__(self):
        print(f'Linked List is being deleted.')

    def __str__(self):
        llist = []
        id_ist = []
        temp = self._head._next
        for _ in range(self._size):
            if temp is self._trailer:
                break
            llist.append(temp._data)
            id_ist.append(temp._id)
            temp = temp._next
        return f'{str(llist)}\nID: {str(id_ist)}'


if __name__ == '__main__':
    d_list = DLL()
    d_list.insert(1, 23)
    d_list.insert(2, 3)
    d_list.insert(3, 4)
    d_list.insert(4, 6)
    d_list.insert(5, -9)
    print(d_list)
    print(d_list.search(23))
