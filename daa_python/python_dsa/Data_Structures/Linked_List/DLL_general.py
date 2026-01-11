class Node:
    __slots__ = 'data', 'next', 'prev'
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        '''this func prints the DLL'''
        temp = self.head
        print('Current Linked List: ', end='')
        while temp:
            print(temp.data, end=', ')
            temp = temp.next
        print('\b\b')

    def insert(self, node, pos):
        '''ths func inserts a node'''
        if pos == 1:
            self.head.prev = node
            node.next = self.head
            self.head = node
            return
        elif pos == self.node_count()+1:
            temp = self.head
            for i in range(pos-2):
                temp = temp.next
            temp.next = node
            node.prev = temp
            return
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
        temp.next.prev = node
        node.next = temp.next
        node.prev = temp
        temp.next = node

    def delete(self, pos):
        '''this func deletes a node'''
        temp = self.head
        if pos == 1:
            self.head = self.head.next
            return temp
        elif pos == self.node_count():
            for i in range(pos-2):
                temp = temp.next
            d_node = temp.next
            temp.next = None
            return d_node
        for i in range(pos-2):
            temp = temp.next
        d_node = temp.next
        d_node.next.prev = temp
        temp.next = d_node.next
        return d_node

    def reverse(self):
        '''this func reverses the DLL'''
        temp = self.head
        j = 1
        n = self.node_count()
        for i in range(n, 0, -1):
            d_node = self.delete(n)
            self.insert(d_node, j)
            j += 1

    def sort(self):
        '''this func sorts the DLL through insertion sort technique'''
        n_nodes = self.node_count()
        small_node = self.smallest_node(1)
        d_node = self.delete(small_node)
        self.insert(d_node, 1)
        for i in range(2, n_nodes):
            small_node = self.smallest_node(i) + i - 1
            d_node = self.delete(small_node)
            self.insert(d_node, i)

    def search(self, val):
        '''this func searches for a value'''
        temp = self.head
        while temp.data != val:
            if temp.next is None:
                return False
            temp = temp.next
        return True

    def node_count(self):
        '''this func returns the node count'''
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def smallest_node(self, start):
        '''this func returns the smallest node'''
        small = self.head
        temp = self.head.next
        if start != 1:
            for i in range(start-1):
                small = small.next
                temp = small.next
        count = 1
        sec = 2
        while temp:
            if small.data > temp.data:
                small = temp
                count = sec
            sec += 1
            temp = temp.next
        return count


if __name__=='__main__':
    l_list = LinkedList()
    while not l_list.head:
        try:
            val = int(input('Enter value [enter 0 when done]: '))
            if not val:
                print('No input\tNo output.')
                exit(0)
            l_list.head = Node(val)
        except ValueError:
            print('Invalid value.')
    temp = l_list.head
    while True:
        try:
            val = int(input('Enter value: '))
            if not val:
                break
            node = Node(val)
            temp.next = node
            node.prev = temp
            temp = temp.next
        except ValueError:
            print('Invalid value.')
            continue
    l_list.print_linked_list()
    while True:
        print('''
    Options: 0. Exit.\t1. insert.\t2. Delete.\t3. Reverse.
    4. Sort.\t5. Search.\t6. Show current DLL
    Enter the assigned index number.''')
        while True:
            try:
                choice = int(input('Enter choice: '))
            except ValueError:
                continue
            else:
                break
        if not choice:
            break
        elif choice == 1:
            val = int(input('Enter value: '))
            if not val:
                print('Invalid value.')
                continue
            pos = int(input('Enter position: '))
            if pos < 1 or pos > l_list.node_count()+1:
                print('Invalid position.')
                continue
            node = Node(val)
            l_list.insert(node, pos)
            l_list.print_linked_list()
        elif choice == 2:
            pos = int(input('Enter position: '))
            if pos < 1 or pos > l_list.node_count():
                print('Invalid position.')
                continue
            l_list.delete(pos)
            l_list.print_linked_list()
        elif choice == 3:
            '''
            temp = l_list.head
            for i in range(l_list.node_count()-1):
                temp = temp.next
            for i in range(l_list.node_count()):
                print(temp.data, end=', ')
                temp = temp.prev
            print('\b\b')
            '''
            l_list.reverse()
            l_list.print_linked_list()
        elif choice == 4:
            l_list.sort()
            l_list.print_linked_list()
        elif choice == 5:
            val = int(input('Enter search value: '))
            if l_list.search(val):
                print('yes')
            else:
                print('no')
        elif choice == 6:
            l_list.print_linked_list()
        else:
            print('Wrong entry!!')
    print('END'.center(80, '.'))
