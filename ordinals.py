#! /usr/local/bin/python3


LT, EQ, GT = -1, 0, 1
def compi(x, y): return EQ if x==y else (LT if x<y else GT)

class Ordinal:
    def __init__(self, *args):
        self.parts = args

    def __str__(self):
        i = self.toInt()
        if i is not None: return str(i)
        elif self == w: return "w"
        else:
            (L, R) = ("(", ")") if len(self.parts) > 1 else ("", "")
            return L+"+".join(f"w^{x}" for x in self.parts)+R

    def comp(self, other):
        if self.isZero(): return EQ if other.isZero() else LT
        if other.isZero(): return GT
        for (x, y) in zip(self.parts, other.parts):
            c = x.comp(y)
            if c != EQ: return c
        return compi(len(self.parts), len(other.parts))

    def __eq__(self, other):
        return len(self.parts) == len(other.parts) and all(x==y for (x,y) in zip(self.parts, other.parts))

    def __lt__(self, other): return self.comp(other) == LT

    def __gt__(self, other): return self.comp(other) == GT

    def __add__(self, other):
        pass    # TODO



    @staticmethod
    def zero(): return Ordinal()

    def isZero(self): return not self.parts

    @staticmethod
    def fromInt(i): return Ordinal(*([zero]*i)) if i else zero

    def toInt(self): return len(self.parts) if all(x.isZero() for x in self.parts) else None


def Ord(*args): return Ordinal(*args)
def n2o(i): return Ordinal.fromInt(i)
zero = Ordinal()
one = n2o(1)
two = n2o(2)
three = n2o(3)
w = Ord(one)



print(Ord(Ord(two), two))
assert three == three
assert three != one
assert three.toInt() == 3
assert one != w
assert one < three
assert w > three

