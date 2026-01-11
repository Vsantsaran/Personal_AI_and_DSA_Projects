# Queue implementation
class Queue:
    def __init__(self):
        self.qu = []

    def __len__(self):
        return len(self.qu)

    def is_empty(self):
        return self.qu == []

    def enqueue(self, num):
        self.qu.append(0)
        for i in range(len(self.qu)-1, 0, -1):
            self.qu[i] = self.qu[i-1]
        self.qu[0] = num

    def dequeue(self):
        if self.is_empty():
            return -1
        return self.qu.pop(0)

    def search(self, num):
        if self.is_empty():
            return -1
        if num in self.qu:
            return self.qu.index(num)

    def __str__(self):
        return f'<{self.qu}>'
