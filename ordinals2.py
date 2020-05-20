#! /usr/local/bin/python3
import math
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

def log(x):
    return x[0]

def bp(x):
    if x is zro: return ""
    (xa, xn, xb) = x
    return ("("+bp(xa)+")")*xn+bp(xb)

def o2i(x) -> float:
    ps = bp(x)
    bit = 1.0
    ret = 0.0
    for p in ps:
        bit /= 2
        if p == "(": ret += bit
    return ret

def slog(x) -> float:
    return -math.log2(1-o2i(x))

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

def normal(x) -> str:
    if x is zro: return True
    (xa, xn, xb) = x
    if xn == 0: return False
    if xa is zro: return xb is zro
    if xb is zro: return normal(xa)
    (xba, xbn, xbb) = xb
    if xbn == 0: return False
    return normal(xa) and normal(xba) and comp(xa, xba) is GT

#### ####

# TODO: memoize/hash-cons

class Ord:
    def __init__(self, val): self.val = val
    def __str__(self): return s(self.val)
    def __hash__(self): return hash(self.val)
    def __eq__(self, other): return self.val == a2o(other).val
    def comp(self, other): return comp(self.val, a2o(other).val)
    def __lt__(self, other): return self.comp(a2o(other)) is LT
    def __gt__(self, other): return self.comp(a2o(other)) is GT
    def __le__(self, other): return self.comp(a2o(other)) is not GT
    def __ge__(self, other): return self.comp(a2o(other)) is not LT
    def __add__(self, other): return Ord(add(self.val, a2o(other).val))
    def __sub__(self, other): return Ord(sub(self.val, a2o(other).val))
    def __mul__(self, other): return Ord(mul(self.val, a2o(other).val))
    def __pow__(self, other): return Ord(exp(self.val, a2o(other).val))
    def tet(self, n): return Ord(tet(self.val, a2n(n)))
    @property
    def bp(self): return bp(self.val)
    @property
    def slog(self): return slog(self.val)
    @property
    def o2i(self): return o2i(self.val)

def n2o(n: int) -> Ord: return Ord(fromInt(n))
def a2o(a: Union[int, Ord]) -> Ord: return a if isinstance(a, Ord) else n2o(a)
def o2n(x: Ord) -> int: return toInt(x.val)
def a2n(a: Union[int, Ord]) -> int: return o2n if isinstance(a, Ord) else a
zero, one, two, three = map(n2o, range(4))
w = Ord((n2o(1).val, 1, zro))
ww = w**w
www = w**ww
wwww = w.tet(4)

def getOrds(pred=None, size=20, lim=www):
    """get all ords satisfying a predicate"""
    pred = pred or (lambda x: len(x.bp) < size and x <= lim)
    ords = {zero}
    while True:
        news = set(ords)
        for x in ords: news.update({x+1, w**x})
        news = set(x for x in news if pred(x))
        if news == ords: break
        ords = news
    return sorted(ords)

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

    # print(zero.bp)
    # print(one.bp)
    # print(two.bp)
    # print(three.bp)
    # print(w.bp)
    # print(www.bp)
    #
    # print(zero.slog)
    # print(one.slog)
    # print(two.slog)
    # print(three.slog)
    # print(w.slog)
    # print(www.slog)

    # a = Ord((one.val, 1, one.val))
    # b = Ord((w.val, 1, one.val))
    # c = Ord((one.val, 1, zero.val))
    # d = Ord((one.val, 1, w.val))
    # print(f"normal({a}): {normal(a.val)}")
    # print(f"normal({b}): {normal(b.val)}")
    # print(f"normal({c}): {normal(c.val)}")
    # print(f"normal({d}): {normal(d.val)}")

    for x in getOrds(): print(x)








