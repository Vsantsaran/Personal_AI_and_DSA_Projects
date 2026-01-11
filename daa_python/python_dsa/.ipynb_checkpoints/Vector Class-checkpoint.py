class Vector:
    def __init__(self, dim):
        self._coords = [0] * dim
        self.dim = len(self)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __len__(self):
        return len(self._coords)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match.')
        res = Vector(len(self))
        for i in range(len(self)):
            res[i] = self[i] + other[i]
        return res

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match.')
        res = Vector(4)
        for i in range(len(self)):
            res[i]  = self[i] - other[i]
        return res

    def __lt__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match.')
        for i in range(len(self)):
            if self[i] >= other[i]:
                return False
        return True

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords) + '>'


v1 = Vector(4)
v2 = Vector(4)
v1[0] = 2
v1[1] = 10
v1[2] = 8
v1[3] = -8
v2[0] = 7
v2[1] = 17
v2[2] = 42
v2[3] = 1

print(v1, v2, sep='\n')
v3 = v1 + v2
print(v3)
print(v1-v2)

if v1 < v2:
    print('<')
else:
    print('>=')
if v1 != v2:
    print('!=')
else:
    print('==')