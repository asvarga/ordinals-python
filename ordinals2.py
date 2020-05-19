#! /usr/local/bin/python3
from typing import List, Tuple, Any

LT, EQ, GT = -1, 0, 1
def compi(x, y): return EQ if x==y else (LT if x<y else GT)

#### ####

## (a, n, b) := w^a*n+b
zero    = None
one     = (zero, 1, zero)
two     = (zero, 2, zero)
three   = (zero, 3, zero)
w       = (one, 1, zero)

#### ####

def comp(x, y):
    if x is zero: return EQ if y is zero else LT
    if y is zero: return GT
    (xa, xn, xb), (ya, yn, yb) = x, y
    cmp = comp(xa, ya)
    if cmp is not EQ: return cmp
    cmpi = compi(xn, yn)
    if cmpi is not EQ: return cmpi
    return comp(xb, yb)

def add(x, y):
    if x is zero: return y
    if y is zero: return x
    (xa, xn, xb), (ya, yn, yb) = x, y
    cmp = comp(xa, ya)
    if cmp is LT: return y
    if cmp is GT: return (xa, xn, add(xb, y))
    return (xa, xn+yn, add(xb, yb))

def sub(x, y):
    """not sure if left or right subtraction"""
    if x is zero: return zero
    if y is zero: return x
    (xa, xn, xb), (ya, yn, yb) = x, y
    cmp = comp(xa, ya)
    if cmp is LT: return zero
    if cmp is GT: return x
    cmpi = compi(xn, yn)
    if cmpi is LT: return zero
    if cmpi is GT: return (xa, xn-yn, xb)
    return sub(xb, yb)

def mul(x, y):
    if x is zero or y is zero: return zero
    (xa, xn, xb), (ya, yn, yb) = x, y
    if ya is zero: return (xa, xn*yn, xb)
    if yb is zero: return (add(xa, ya), yn, zero)
    return add(mul(x, (ya, yn, zero)), mul(x, yb))

def exp(x, y): pass # TODO

#### ####

# TODO: memoize/hash-cons

class Ord:
    def __init__(self, val): self.val = val
    def __eq__(self, other): return self.val == other.val
    def comp(self, other): return comp(self.val, other.val)
    def __lt__(self, other): return self.comp(other) == LT
    def __gt__(self, other): return self.comp(other) == GT
    def __add__(self, other): return Ord(add(self.val, other.val))
    def __sub__(self, other): return Ord(sub(self.val, other.val))
    def __mul__(self, other): return Ord(mul(self.val, other.val))

def n2o(i: int) -> Ord: return Ord((zero, i, zero))

#### ####

if __name__ == "__main__":
    print(123)








