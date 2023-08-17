from rational import Rational
from matrix import Matrix, Lie, zeroData

N = 4 # set this as you want!

# sl2 triple f, e, h (see Arakawa note p.4)
f = zeroData(N)
for i in range(0, N - 1):
    f[i + 1][i] = 1
f = Matrix(f)

e = zeroData(N)
for i in range(0, N - 1):
    e[i][i + 1] = (i + 1) * (N - (i + 1))
e = Matrix(e)

h = zeroData(N)
for i in range(0, N):
    h[i][i] = (N + 1 - 2 * (i + 1))
h = Matrix(h)


# Killing form
def trace(X):
    ret = 0
    for i in range(0, N):
        ret += X.getData()[i][i]
    return ret

def Killing(X, Y):
    return 2 * N * trace(X * Y)

# basis
# REQUIREMENT: must has a Kazhdan degree
def base(k):
    assert type(k) == int
    assert k >= 0
    assert k < N * N - 1
    i = k // N
    j = k % N

    data = zeroData(N)
    if i == j:
        data[i][i] = 1
        data[i + 1][i + 1] = -1
    else:
        data[i][j] = 1
    
    return Matrix(data)

def KazhdanDeg(mat):
    if mat.isZero():
        return 0
    else:
        comm = Lie(h, mat)
        size = mat.getSize()
        eigenval = None
        C = comm.getData()
        M = mat.getData()

        deg = None
        found = False
        for i in range(0, size):
            for j in range(0, size):
                if not M[i][j] == 0:
                    eigenval = C[i][j] / M[i][j]
                    found = True
                    break
            if found:
                break
        
        assert Lie(h, mat) == eigenval @ mat
        deg = int(Rational(1, 2) * eigenval)
        return deg


# structure coeffs
def coeff(X, k):
    i = k // N
    j = k % N

    if i == j:
        ret = 0
        for t in range(0, i + 1):
            ret += X.getData()[t][t]
        return ret
    else:
        return X.getData()[i][j]


def structCoeff(a, b, c): # [x_a, x_b] == c_ab^c x_c
    return coeff(Lie(base(a), base(b)), c)


# test
if __name__ == "__main__":
    assert Lie(h, h).isZero()
    assert Lie(e, e).isZero()
    assert Lie(f, f).isZero()

    assert Lie(h, e) == 2 @ e
    assert Lie(h, f) == -2 @ f
    assert Lie(e, f) == h
    print("Serre relation : OK")


    for i in range(0, N * N - 1):
        KazhdanDeg(base(i)) # check whether deg is in Z
    print("Kazhdan degree : OK")


    for a in range(0, N * N - 1):
        for b in range(0, N * N - 1):
            result = Matrix(zeroData(N))
            for c in range(0, N * N - 1):
                result = result + structCoeff(a, b, c) @ base(c)
            assert result == Lie(base(a), base(b))
    print("structure coeff: OK")

