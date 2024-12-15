''' This document id created to practice complex datatype
created by Peddakotla Hari created on 02/12/2024
'''

a = 3.0 + 4j # 3.0 is a real number, 4 is the imag number and j is sqrt(-1)

print("Value of a",a)
print("DataType for a = ",type(a))
print("Storage allocation for a = ",id(a))

print()
ab = 3.0 + 4j
print("Value of ab",ab)
print("DataType for ab = ",type(ab))
print("Storage allocation for ab = ",id(ab))

print()
abc = 4j
print("Value of abc",abc)
print("DataType for abc = ",type(abc))
print("Storage allocation for abc = ",id(abc))

print()
p = False
print("Value of p is ",p)
print("DataType of p is",type(p))
print("Storage allocation for p is",id(p))

print()

q = True
print("Value of q is ",q)
print("DataType of q is",type(q))
print("Storage allocation for q is",id(q))

print()

r = True
print("Value of r is ",r)
print("DataType of r is",type(r))
print("Storage allocation for r is",id(r))

print()

s = False
print("Value of s is ",s)
print("DataType of s is",type(s))
print("Storage allocation for s is",id(s))

print(f"addition of {p}, {r}",r.__add__(r))