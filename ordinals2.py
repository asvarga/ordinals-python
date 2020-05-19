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

def exp(x, y): pass # TODO

def width(x) -> int:
    if x is zro: return 0
    (xa, xn, xb) = x
    return xn+width(xb)

def fromInt(n: int):
    return (zro, n, zro) if n else zro

def toInt(x) -> Optional[int]:
    if x is zro: return 0
    (xa, xn, xb) = x
    return xn if xa is zro else None

def parens(x) -> bool:
    return toInt(x) is None and width(x) > 1

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

def n2o(n: int) -> Ord: return Ord(fromInt(n))
def a2o(a: Union[int, Ord]) -> Ord: return a if isinstance(a, Ord) else n2o(a)
zero, one, two, three = map(n2o, range(4))
w = Ord((n2o(1).val, 1, zro))
ww = Ord((w.val, 1, zro))
www = Ord((ww.val, 1, zro))

#### ####

if __name__ == "__main__":
    # print(w.val)
    # print(zero)
    # print(one)
    # print(two)
    # print(w)
    print(w+1)
    print(one+w)
    print(w+w)
    print(w*w)
    print(three*w)
    print(w*3)
    print(ww)
    print(www)







