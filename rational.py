
def gcd0(a, b): # assume a >= b >= 0
    if b == 0:
        return a
    else:
        c = a % b
        if c == 0:
            return b
        else:
            return gcd0(b, c)

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a >= b:
        return gcd0(a, b)
    else:
        return gcd0(b, a)

class Rational:
    def __init__(self, numerator, dominator = 1):
        assert type(numerator) == int
        assert type(dominator) == int
        assert dominator != 0

        self.numerator = numerator
        self.dominator = dominator

    def getNum(self):
        return self.numerator
    
    def getDom(self):
        return self.dominator
    
    def __eq__(self, x):
        if type(x) == int:
            x = Rational(x)
        return self.getNum() * x.getDom() == self.getDom() * x.getNum()

    def __neg__(self):
        num = -self.getNum()
        dom = self.getDom()
        return Rational(num, dom)

    def __add__(self, x):
        if type(x) == int:
            x = Rational(x)
        
        num = self.getNum() * x.getDom() + self.getDom() * x.getNum()
        dom = self.getDom() * x.getDom()
        return Rational(num, dom)

    def __radd__(self, x):
        if type(x) == int:
            x = Rational(x)
        
        num = self.getNum() * x.getDom() + self.getDom() * x.getNum()
        dom = self.getDom() * x.getDom()
        return Rational(num, dom)
    
    def __sub__(self, x):
        return self + (-x)
    
    def __rsub__(self, x):
        return self + (-x)

    def __mul__(self, x):
        if type(x) == int:
            x = Rational(x)

        num = self.getNum() * x.getNum()
        dom = self.getDom() * x.getDom()
        return Rational(num, dom)

    def __rmul__(self, x):
        if type(x) == int:
            x = Rational(x)

        num = self.getNum() * x.getNum()
        dom = self.getDom() * x.getDom()
        return Rational(num, dom)

    def __truediv__(self, x):
        if type(x) == int:
            x = Rational(x)

        num = self.getNum() * x.getDom()
        dom = self.getDom() * x.getNum()
        return Rational(num, dom)

    def __rtruediv__(self, x):
        if type(x) == int:
            x = Rational(x)

        num = self.getNum() * x.getDom()
        dom = self.getDom() * x.getNum()
        return Rational(num, dom)

    def __pow__(self, x):
        assert type(x) == int
        
        num = self.getNum() ** x
        dom = self.getDom() ** x
        return Rational(num, dom)

    def __str__(self):
        num = self.getNum()
        dom = self.getDom()

        if num == 0:
            return str(0)
        if num % dom == 0:
            return str(num // dom)
        else:
            g = gcd(num, dom)
            num //= g
            dom //= g
            ret = ""
            if num * dom < 0:
                ret += "-"
            num = abs(num)
            dom = abs(dom)
            ret += str(num)
            ret += "/"
            ret += str(dom)
            return ret

    def __hash__(self):
        return hash((self.numerator(), self.dominator()))
    
    def __int__(self):
        num = self.getNum()
        dom = self.getDom()

        assert num % dom == 0
        return num // dom


# test
if __name__ == "__main__":
    expect = (2/3) + 3 * (5/2) - (1/6) / (1/3)
    result = eval(str(Rational(2, 3) + 3 * Rational(5, 2) - Rational(1, 6) / Rational(1, 3)))

    print("expect : " + str(expect))
    print("result : " + str(result))

    print("14 / (-21) = " + str(Rational(14, -21)))

