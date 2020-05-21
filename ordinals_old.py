#! /usr/local/bin/python3
from typing import List, Tuple, Any

LT, EQ, GT = -1, 0, 1
def compi(x, y): return EQ if x==y else (LT if x<y else GT)

#### ####

class Ordinal:
    def __init__(self, *args):
        # assert self == sum(w^x*c for (x,c) in self.parts)
        self.parts: List[Tuple[Ordinal], int] = list(args)

    def toLists(self) -> List[Any]: return [(x.toLists(),c) for (x,c) in self.parts]

    def __repr__(self) -> str: return str(self.toLists())

    @staticmethod
    def pp(x,c) -> str:
        """pretty print w^x*c"""
        if x.isZero(): return str(c)
        if x == one: return "w" if c==1 else f"w*{c}"
        if x.parens(): return f"w^({x})" if c==1 else f"w^({x})*{c}"
        return f"w^{x}" if c==1 else f"w^{x}*{c}"

    def parens(self) -> bool: return self.toInt() is None and self.width() > 1

    def __str__(self): return "0" if self.isZero() else "+".join(Ordinal.pp(x,c) for (x,c) in self.parts)

    def width(self) -> int: return sum(c for (x,c) in self.parts)

    def comp(self, other) -> int:
        for ((x,c), (y,d)) in zip(self.parts, other.parts):
            cmp = x.comp(y)
            if cmp is not EQ: return cmp
            cmpi = compi(c, d)
            if cmpi is not EQ: return cmpi
        return compi(len(self.parts), len(other.parts))

    def __eq__(self, other) -> bool: return self.parts == other.parts

    def __lt__(self, other) -> bool: return self.comp(other) == LT

    def __gt__(self, other) -> bool: return self.comp(other) == GT

    def __add__(self, other):
        if other.isZero(): return self
        ps, qs = self.parts, other.parts
        (y,d) = qs[0]
        # TODO: binary search
        for (i, (x,c)) in enumerate(ps):
            cmp = x.comp(y)
            if cmp is EQ: return Ordinal(*(ps[:i]+[(x, c+d)]+qs[1:]))
            if cmp is LT: return Ordinal(*(ps[:i]+qs))
        return Ordinal(*(ps+qs))

    def __sub__(self, other):
        ps, qs = self.parts, other.parts
        for (i, ((x,c), (y,d))) in enumerate(zip(ps, qs)):
            cmp = x.comp(y)
            if cmp is LT: return zero
            if cmp is GT: return Ordinal(*ps[i:])
            cmpi = compi(c, d)
            if cmpi is LT: return zero
            if cmpi is GT: return Ordinal(*([(x,c-d)]+ps[i+1:]))
        return 

        # if other.isZero() or self.isZero(): return self
        # TODO

    def __mul__(self, other): pass # TODO

    @staticmethod
    def zero(): return Ordinal()

    def isZero(self) -> bool: return not self.parts

    @staticmethod
    def fromInt(i: int): return Ordinal((zero, i)) if i else zero

    def toInt(self) -> int:
        if self.isZero(): return 0
        if len(self.parts) == 1 and self.parts[0][0].isZero(): return self.parts[0][1]

def Ord(*args): return Ordinal(*args)
def n2o(i): return Ordinal.fromInt(i)
zero = Ordinal()
one = n2o(1)
two = n2o(2)
three = n2o(3)
w = Ord((one,1))


if __name__ == "__main__":
    a = Ord((one, 2), (zero, 1))
    b = Ord((two, 1))
    c = Ord((b, 1), (two, 1))
    # print(a)
    # print(w)
    # print(b)
    # print(c)

    assert a < b
    assert b < c

    print(f"{a} + {b} = {a + b}") # assert a + b == w^2
    print(f"{b} + {a} = {b + a}") # assert b + a == w^2+w*2+1
    print(f"{a} + {c} = {a + c}") # assert a + c == w^w^2+w^2
    print(f"{c} + {a} = {c + a}") # assert c + a == w^w^2+w^2+w*2+1
    print(f"{b} + {c} = {b + c}") # assert b + c == w^w^2+w^2
    print(f"{c} + {b} = {c + b}") # assert c + b == w^w^2+w^2*2


    assert three == three
    assert three != one
    assert n2o(5) == n2o(5)
    assert three.toInt() == 3
    assert one != w
    assert one < three
    assert w > three

