## Я только сейчас понял, что надо было делать все задачи easy-hard, ну да ладно :(

import numpy as np
from typing import List

## Easy

class Matrix:
    def __init__(self, values : List[List[int]]):
        assert len(values) > 0

        n = len(values)
        m = len(values[0])

        for i in range(n):
            assert len(values[i]) == m

        self.values = values
        self.n = n
        self.m = m

    def __add__(self, other):
        assert self.n == other.n and self.m == other.m

        new = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.values[i][j] + other.values[i][j])
            new.append(row)

        return new


    def __mul__(self, other):
        assert self.n == other.n and self.m == other.m

        new = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.values[i][j] * other.values[i][j])
            new.append(row)

        return new

    def __matmul__(self, other):
        assert self.m == other.n

        new = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                value = 0
                for k in range(self.m):
                    value += self.values[i][k] * other.values[k][j]
                row.append(value)
            new.append(row)

        return new

    def __str__(self):
        return '\n'.join(['\t'.join([str(value) for value in row]) for row in self.values])


np.random.seed(0)

m1 = np.random.randint(0, 10, (10, 10))
m2 = np.random.randint(0, 10, (10, 10))

a = Matrix(m1)
b = Matrix(m2)

with open('artifacts/easy/matrix+.txt', 'w') as f:
    f.write(str(a + b))

with open('artifacts/easy/matrix*.txt', 'w') as f:
    f.write(str(a * b))

with open('artifacts/easy/matrix@.txt', 'w') as f:
    f.write(str(a @ b))   


# Meidum - Hard

class Matrix_np:
    def __init__(self, values : np.ndarray):
        self._values = values    

    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self, new_values):
        self._values = new_values

    def __add__(self, other):
        return Matrix_np(self.values + other.values)

    def __sub___(self, other):
        return Matrix_np(self.values - other.values)
    
    def __mul__(self, other):
        return Matrix_np(self.values * other.values)

    def __matmul__(self, other):
        return Matrix_np(self.values @ other.values)

    def __truediv__(self, other):
        return Matrix_np(self.values / other.values)
    
    def __mod__(self, other):
        return Matrix_np(self.values % other.values)
    
    def __divmod__(self, other):
        return Matrix_np(np.divmod(self.values, other.values))
    
    def __pow__(self):
        return Matrix_np(np.pow(self.values))
    
    def __lshift__(self, k):
        return Matrix_np(self.values << k)
    
    def __rshift__(self, k):
        return Matrix_np(self.values >> k)
    
    def __and__(self, other):
        return Matrix_np(self.values & other.values)
    
    def __xor__(self, other):
        return Matrix_np(self.values ^ other.values)

    def __or__(self, other):
        return Matrix_np(self.values | other.values)

    def __eq__(self, other):
        return np.equal(self.values, other.values).all()
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def to_file(self, filename):
        with open(filename, 'w') as fout:
            fout.write(str(self))

    def __str__(self):
        return '\n'.join(['\t'.join([str(value) for value in row]) for row in self.values])

    # Прибавляю к результату следующее значение матрицы, умноженное на результат предыдущей итерации и плюс номер итерации
    # По модулю простого числа
    def __hash__(self):
        f = self.values.flatten()
        hash = f[0]
        for i in range(1, len(f)):
            hash = (hash + f[i] * hash + i) % 1046527

        return int(hash)
    

a = Matrix_np(m1)
b = Matrix_np(m2)

(a + b).to_file('artifacts/medium/matrix+.txt')
(a * b).to_file('artifacts/medium/matrix*.txt')
(a @ b).to_file('artifacts/medium/matrix@.txt')

## Ищу матрицы для Hard

k = 10

a = Matrix_np(np.random.randint(0, 10, (k, k)))
b = Matrix_np(np.random.randint(0, 10, (k, k)))

while True:
    c = Matrix_np(np.random.randint(0, 10, (k, k)))

    if hash(a) == hash(c) and a != c and (a @ b) != (c @ b): 
        a.to_file('artifacts/hard/A.txt')
        b.to_file('artifacts/hard/B.txt')
        c.to_file('artifacts/hard/C.txt')
        b.to_file('artifacts/hard/D.txt')
        (a @ b).to_file('artifacts/hard/AB.txt')
        (c @ b).to_file('artifacts/hard/CD.txt')

        with open('artifacts/hard/hash.txt', 'w') as fout:
            fout.write(str(hash(a * b)) + '\n' + str(hash(c * b)))
        break
