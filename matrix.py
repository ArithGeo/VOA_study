from rational import Rational

class Matrix: # squares only
    def __init__(self, input):
        data = []
        
        assert type(input) == list
        size = len(input)
        self.size = size

        for row in input:
            assert type(row) == list
            assert len(row) == size
            row1 = []
            for value in row:
                if type(value) == int:
                    row1.append(Rational(value))
                else:
                    assert type(value) == Rational
                    row1.append(value)
            data.append(tuple(row1))
        self.data = data

    def getSize(self):
        return self.size
    
    def getData(self):
        return self.data

    def isZero(self):
        for row in self.getData():
            for value in row:
                if not value == 0:
                    return False
        return True
    
    def __eq__(self, X):
        return (self - X).isZero()

    def __neg__(self):
        size = self.getSize()
        A = self.getData()

        data = []

        for i in range(0, size):
            data.append([])
            for j in range(0, size):
                data[i].append(-A[i][j])
        
        return Matrix(data)
        
    def __add__(self, X):
        size = self.getSize()
        assert size == X.getSize()

        A = self.getData()
        B = X.getData()

        data = []
        for i in range(0, size):
            data.append([])
            for j in range(0, size):
                data[i].append(A[i][j] + B[i][j])
        
        return Matrix(data)

    def __sub__(self, X):
        return self + (-X)

    def __mul__(self, X):
        size = self.getSize()
        assert size == X.getSize()

        A = self.getData()
        B = X.getData()
        
        data = []
        for i in range(0, size):
            data.append([])
            for j in range(0, size):
                data[i].append(0)

        for i in range(0, size):
            for j in range(0, size):
                for k in range(0, size):
                    data[i][j] += (A[i][k] * B[k][j])

        return Matrix(data)

    def __rmatmul__(self, x):
        if type(x) == int:
            x = Rational(x)
        assert type(x) == Rational

        size = self.getSize()
        A = self.getData()

        data = []
        for i in range(0, size):
            data.append([])
            for j in range(0, size):
                data[i].append(A[i][j] * x)

        return Matrix(data)

    def __str__(self):
        size = self.getSize()
        distance = 10
        A = self.getData()
        marker = "-" * distance

        ret = ""
        ret += marker
        ret += "\n"
        for i in range(0, size):
            for j in range(0, size):
                result = str(A[i][j])
                ret += result
                ret += ","
                ret += " " * (distance - len(result))
            ret += "\n"
        ret += marker
        return ret
    
    def __hash__(self):
        return hash(self.getData())
    
def Lie(A, B):
    return A * B - B * A

def zeroData(size):
    ret = []
    for _ in range(0, size):
        ret.append([0] * size)
    return ret


# test
if __name__ == "__main__":
    A = Matrix([
        [1, 2],
        [0, 1]
    ])

    B = Matrix([
        [0, 1],
        [1, 0]
    ])

    C = Matrix([
        [1, Rational(1, 2)],
        [1, Rational(1, 2)]
    ])

    # 3 * (A - B * C)
    answer = Matrix([
        [0, Rational(9, 2)],
        [-3, Rational(3, 2)]
    ])

    print("expect : ")
    print(answer)

    print("result : ")
    print(3 @ (A - B * C))


