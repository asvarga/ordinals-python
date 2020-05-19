#! /usr/local/bin/python3


LT, EQ, GT = -1, 0, 1
def compi(x, y): return EQ if x==y else (LT if x<y else GT)

#### ####

class Ordinal:
    def __init__(self, *args):
        self.parts = args

    def toLists(self): return [(c,x.toLists()) for (c,x) in self.parts]

    def __repr__(self): return str(self.toLists())

    @staticmethod
    def pp(c, x):
        """pretty print w^x*c"""
        if x.isZero(): return str(c)
        if x == one: return "w" if c==1 else f"w*{c}"
        if x.parens(): return f"w^({x})" if c==1 else f"w^({x})*{c}"
        return f"w^{x}" if c==1 else f"w^{x}*{c}"

    def parens(self): return self.toInt() is None and self.width() > 1

    def __str__(self): return "0" if self.isZero() else "+".join(Ordinal.pp(c,x) for (c,x) in self.parts)

    def width(self): return sum(c for (c,x) in self.parts)

    def comp(self, other):
        for ((c,x), (d,y)) in zip(self.parts, other.parts):
            cmp = x.comp(y)
            if cmp != EQ: return cmp
            cmpi = compi(c, d)
            if cmpi != EQ: return cmpi
        return compi(len(self.parts), len(other.parts))

    def __eq__(self, other): return self.parts == other.parts

    def __lt__(self, other): return self.comp(other) == LT

    def __gt__(self, other): return self.comp(other) == GT

    # def __add__(self, other):
    #     i,j = 0,0
    #     ret = []
    #     while



    @staticmethod
    def zero(): return Ordinal()

    def isZero(self): return not self.parts

    @staticmethod
    def fromInt(i): return Ordinal((i,zero)) if i else zero

    def toInt(self):
        if self.isZero(): return 0
        if len(self.parts) == 1 and self.parts[0][1].isZero(): return self.parts[0][0]

def Ord(*args): return Ordinal(*args)
def n2o(i): return Ordinal.fromInt(i)
zero = Ordinal()
one = n2o(1)
two = n2o(2)
three = n2o(3)
w = Ord((1,one))


print(Ord((2,one), (1,zero)))
print(w)
print(Ord((1, two)))
print(Ord((1, Ord((1, two))), (1, two)))

assert three == three
assert three != one
assert n2o(5) == n2o(5)
assert three.toInt() == 3
assert one != w
assert one < three
assert w > three

