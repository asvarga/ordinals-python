
from ordinals2 import *


if __name__ == "__main__":

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