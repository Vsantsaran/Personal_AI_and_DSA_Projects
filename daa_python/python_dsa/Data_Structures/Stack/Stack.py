# Stack implementation
class Stack:
    def __init__(self):
        self.stk = []

    def __len__(self):
        return len(self.stk)

    def is_empty(self):
        return self.stk == []

    def push(self, num):
        self.stk.append(num)

    def pop(self):
        if self.stk is self.is_empty():
            return -1
        return self.stk.pop()

    def peek(self):
        if self.stk is self.is_empty():
            return -1
        return self.stk[-1]

    def search(self, val):
        if self.stk is self.is_empty():
            return -1
        if val in self.stk:
            return self.stk.index(val)
        return -2

    def __str__(self):
        return f'<{self.stk}>'

temp = Stack()
temp.push(12)
print(len(temp))
print(temp)