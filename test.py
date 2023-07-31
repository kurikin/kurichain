from ecc import FE, Point

# test.py
p = 65537
a = FE(0, p)
b = FE(7, p)

xP = FE(40192, p)
yP = FE(28715, p)

xQ = FE(10572, p)
yQ = FE(3699, p)

P = Point(xP, yP, a, b)
Q = Point(xQ, yQ, a, b)
O = Point(None, None, a, b)

print(P + O)
print(O + P)
print(O - P)
print(P - O)
