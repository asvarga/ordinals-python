#! /usr/local/bin/python3
from typing import List, Tuple, Any, Optional, Union

LT, EQ, GT = -1, 0, 1
def compi(x, y): return EQ if x==y else (LT if x<y else GT)

#### ####

## (a, n, b) := w^a*n+b
zro = None

def comp(x, y):
    if x is zro: return EQ if y is zro else LT
    if y is zro: return GT
    (xa, xn, xb), (ya, yn, yb) = x, y
    cmp = comp(xa, ya)
    if cmp is not EQ: return cmp
    cmpi = compi(xn, yn)
    if cmpi is not EQ: return cmpi
    return comp(xb, yb)

def add(x, y):
    if x is zro: return y
    if y is zro: return x
    (xa, xn, xb), (ya, yn, yb) = x, y
    cmp = comp(xa, ya)
    if cmp is LT: return y
    if cmp is GT: return (xa, xn, add(xb, y))
    return (xa, xn+yn, add(xb, yb))

def sub(x, y):
    """not sure if left or right subtraction"""
    if x is zro: return zro
    if y is zro: return x
    (xa, xn, xb), (ya, yn, yb) = x, y
    cmp = comp(xa, ya)
    if cmp is LT: return zro
    if cmp is GT: return x
    cmpi = compi(xn, yn)
    if cmpi is LT: return zro
    if cmpi is GT: return (xa, xn-yn, xb)
    return sub(xb, yb)

def mul(x, y):
    if x is zro or y is zro: return zro
    (xa, xn, xb), (ya, yn, yb) = x, y
    if ya is zro: return (xa, xn*yn, xb)
    if yb is zro: return (add(xa, ya), yn, zro)
    return add(mul(x, (ya, yn, zro)), mul(x, yb))

def exp(x, y):
    # print(f"(x, y): {(s(x), s(y))}")
    if y is zro: return one.val         # x^0 = 1
    if x is zro: return zro             # 0^y = 0
    if x is one.val: return one.val     # 1^y = 1
    (xa, xn, xb), (ya, yn, yb) = x, y
    if ya is zro:                       # x^n = x*...*x with fast exp
        sqrt = exp(x, fromInt(yn//2))
        ret = mul(sqrt, sqrt)
        return mul(x, ret) if yn%2 else ret
    if xa is zro and yn == 1 and yb is zro:         # n^(w^ya) = w^(w^(ya-1)), ex: 2^(w^4) = w^(w^3)
        return ((sub(ya, one.val), 1, zro), 1, zro)
    if xa is not zro:                               # (w^xa)^y = w^(xa*y), ex: (w^w)^3 = w^(w*3)
        return (mul(xa, y), 1, zro)
    if yb is zro:                                   # x^(ya*yn) = (x^ya)^yn
        return exp(exp(x, (ya, 1, zro)), fromInt(yn))
    return mul(exp(x, (ya, yn, zro)), exp(x, yb))   # x^(yan+yb) = x^yan * x^yb

def tet(x, n: int):
    return one.val if n == 0 else exp(x, tet(x, n-1))

def width(x) -> int:
    if x is zro: return 0
    (xa, xn, xb) = x
    return xn+width(xb)

def fromInt(n: int):
    return (zro, n, zro) if n else zro

def isInt(x) -> bool:
    return x is zro or x[0] is zro

def toInt(x) -> Optional[int]:
    if x is zro: return 0
    (xa, xn, xb) = x
    return xn

def parens(x) -> bool:
    return not isInt(x) and width(x) > 1

def pp(x, n: int) -> str:
    """pretty print w^x*n"""
    if x is zro: return str(n)
    if x == one.val: return "w" if n==1 else f"w*{n}"
    if parens(x): return f"w^({s(x)})" if n==1 else f"w^({s(x)})*{n}"
    return f"w^{s(x)}" if n==1 else f"w^{s(x)}*{n}"

def parts(x) -> List[Tuple[Any, int]]:
    ret = []
    while x is not zro:
        (xa, xn, xb) = x
        ret.append((xa, xn))
        x = xb
    return ret

def s(x) -> str:
    if x is zro: return "0"
    return "+".join(pp(x,n) for (x,n) in parts(x))

#### ####

# TODO: memoize/hash-cons

class Ord:
    def __init__(self, val): self.val = val
    def __str__(self): return s(self.val)
    def __eq__(self, other): return self.val == a2o(other).val
    def comp(self, other): return comp(self.val, a2o(other).val)
    def __lt__(self, other): return self.comp(a2o(other)) is LT
    def __gt__(self, other): return self.comp(a2o(other)) is GT
    def __add__(self, other): return Ord(add(self.val, a2o(other).val))
    def __sub__(self, other): return Ord(sub(self.val, a2o(other).val))
    def __mul__(self, other): return Ord(mul(self.val, a2o(other).val))
    def __pow__(self, other): return Ord(exp(self.val, a2o(other).val))
    def tet(self, n): return Ord(tet(self.val, a2n(n)))

def n2o(n: int) -> Ord: return Ord(fromInt(n))
def a2o(a: Union[int, Ord]) -> Ord: return a if isinstance(a, Ord) else n2o(a)
def o2n(x: Ord) -> int: return toInt(x.val)
def a2n(a: Union[int, Ord]) -> int: return o2n if isinstance(a, Ord) else a
zero, one, two, three = map(n2o, range(4))
w = Ord((n2o(1).val, 1, zro))
ww = w**w
www = w**ww
wwww = w.tet(4)

#### ####

if __name__ == "__main__":

    # print(w+1)
    # print(one+w)
    # print(w+w)
    # print(w*w)
    # print(three*w)
    # print(w*3)
    # print(ww)
    # print(www)
    # print(w**3)
    # print(w**w)
    # print(w**w**w)
    # print(w**3**2)
    # print((w+1)**(w+1))
    # print(ww)
    # print(www)
    # print(wwww)

    a = w**2*12 + w*3 + 5
    b = w**2*12 + w*4 + 5
    c = w**a*12 + w**2 + w*7 + 3
    d = w**b*12 + w**2 + w*7 + 3
    e = w**3 + w
    f = w**5 + w**3

    # print((w**3 + w)**5)
    # print((w**5 + w**3)**3)
    # print("----")
    # print(one + w)
    # print(c)
    # print(d)
    # print(c + d)
    # print("----")
    # print(a)
    # print(b)
    # print(b - a)
    # print("----")
    # print((w**4*3 + w**3*2 + w**2 + w**1*10 + 100)**5)
    # print((w**w + w**3*2 + w**2)**2)
    # print((w+2)**0)
    # print((w+2)**1)
    # print((w+2)**2)
    # print((w+2)**3)
    # print((w+2)**4)
    # print((w+2)**5)
    # print("----")
    # print(two**zero)
    # print(two**w)
    # print(two**(w*3 + 3))
    # print(two**(w**4 + w**3 + 5))
    # print("----")
    # print(two**(w**w))
    # print(w**(w**w))
    # print((w**w)**(w**w))
    # print((w**w)**2)
    # print((w**w)**w)
    # print(((w**w)*3)**2)
    # print("----")
    # print((w*w+2)**w)
    # print(w*(w**2))
    # print(zero**1)

    assert (w**3 + w)**5 == w**15 + w**13
    assert (w**5 + w**3)**3 == w**15 + w**13

    assert one + w == w
    assert c == w**(w**2*12 + w*3 + 5)*12 + w**2 + w*7 + 3
    assert d == w**(w**2*12 + w*4 + 5)*12 + w**2 + w*7 + 3
    assert c + d == w**(w**2*12 + w*4 + 5)*12 + w**2 + w*7 + 3

    assert a == w**2*12 + w*3 + 5
    assert b == w**2*12 + w*4 + 5
    assert b - a == w + 5

    assert (w**4*3 + w**3*2 + w**2 + w**1*10 + 100)**5 == w**20*3 + w**19*2 + w**18 + w**17*10 + w**16*300 + w**15*2 + w**14 + w**13*10 + w**12*300 + w**11*2 + w**10 + w**9*10 + w**8*300 + w**7*2 + w**6 + w**5*10 + w**4*300 + w**3*2 + w**2 + w*10 + 100
    assert (w**w + w**3*2 + w**2)**2 == w**(w*2) + w**(w + 3)*2 + w**(w + 2)
    assert (w+2)**0 == 1
    assert (w+2)**1 == w + 2
    assert (w+2)**2 == w**2 + w*2 + 2
    assert (w+2)**3 == w**3 + w**2*2 + w*2 + 2
    assert (w+2)**4 == w**4 + w**3*2 + w**2*2 + w*2 + 2
    assert (w+2)**5 == w**5 + w**4*2 + w**3*2 + w**2*2 + w*2 + 2

    assert two**zero == 1
    assert two**w == w
    assert two**(w*3 + 3) == w**3*8
    assert two**(w**4 + w**3 + 5) == w**(w**3 + w**2)*32

    assert two**(w**w) == w**(w**(w))
    assert w**(w**w) == w**(w**(w))
    assert (w**w)**(w**w) == w**(w**(w))
    assert (w**w)**2 == w**(w*2)
    assert (w**w)**w == w**(w**2)
    assert ((w**w)*3)**2 == w**(w*2)*3

    assert (w*w+2)**w == w**(w)
    assert w*(w**2) == w**3
    assert zero**1 == 0







