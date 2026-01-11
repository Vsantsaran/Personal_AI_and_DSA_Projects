# Binary tree - inorder traversal
class Node(object):
    '''this class makes a node'''
    emp_id = 1001

    def __init__(self, data):
        self.data = data
        self.ID = Node.emp_id
        self.left = None
        self.right = None
        Node.emp_id += 1


class BinaryTree(object):
    '''Binary Tree Sort though in-order-traversal'''
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        if root is None:
            return node
        if node.data <= root.data:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)
        return root

    def in_order_traverse(self, root):
        '''this func traverses the whole binary tree'''
        if root:
            self.in_order_traverse(root.left)
            print(f'Value: {root.data}\t\t\tID: {root.ID}')
            self.in_order_traverse(root.right)


if __name__ == '__main__':
    bin_tree = BinaryTree()
    while bin_tree.root is None:
        try:
            val = int(input('Enter value: '))
            if not val:
                print('No input.\tNo output.')
                exit(0)
            bin_tree.root = bin_tree.insert(bin_tree.root, Node(val))
        except ValueError:
            print('Invalid value!!')
            continue
    while True:
        try:
            val = int(input('Enter value: '))
            if not val:
                break
            node = Node(val)
            bin_tree.insert(bin_tree.root, node)
        except ValueError:
            print('Invalid value!!')
            continue
    bin_tree.in_order_traverse(bin_tree.root)
    while True:
        print('''\
    Options: 0. Exit.\t1. Insert.\t2. Show current Binary Tree.
    Enter the assigned value to the option.''')
        choice = int(input('Enter choice: '))
        if not choice:
            break
        elif choice == 1:
            try:
                val = int(input('Enter value: '))
                if not val:
                    print('Invalid value.')
                    continue
                node = Node(val)
                bin_tree.insert(bin_tree.root, node)
                bin_tree.in_order_traverse(bin_tree.root)
            except ValueError:
                print('Invalid value!!')
                continue
        elif choice == 2:
            bin_tree.in_order_traverse(bin_tree.root)
        else:
            print('Wrong entry!!')
    print('END'.center(80, '.'))
