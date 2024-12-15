""" This Document is crated to practice on LogicaL operators
Created by Peddakotla Hari on 11/12/2024"""

# a       b       AND     OR
# False   False   False   False
# True    False   False   True
# False   True    False   True
# True    True    True    True

# a   b   AND OR
# 0   0   0   0
# 0   1   0   1
# 1   0   0   1
# 1   1   1   1

print(f"bool(0):",bool(0))
print(f"bool(1):",bool(1))
print(f"bool(10):",bool(10))
print(f"bool(20):",bool(20))
print(f"bool(13):",bool(13))

print("~"*20,f"Logical Operator AND. EX:1 ","~"*20)
a = 12
b = 23
print(f"bool(a):",bool(a))
print(f"bool(b):",bool(b))
print(f"bool(a) and bool(b) :",bool(a) and bool(b))

print("~"*20,f"Logical Operator AND. EX:2 ","~"*20)
a = 0
b = 23
print(f"bool(a):",bool(a))
print(f"bool(b):",bool(b))
print(f"bool(a) and bool(b) :",bool(a) and bool(b))

print("~"*20,f"Logical Operator AND. EX:3 ","~"*20)
a = 0
b = 0
print(f"bool(a):",bool(a))
print(f"bool(b):",bool(b))
print(f"bool(a) and bool(b) :",bool(a) and bool(b))

print("~"*20,f"Logical Operator OR. EX:1 ","~"*20)
a = 0
b = 0
print(f"bool(a):",bool(a))
print(f"bool(b):",bool(b))
print(f"bool(a) OR bool(b) :",bool(a) or bool(b))

print("~"*20,f"Logical Operator OR. EX:2 ","~"*20)
a = 0
b = 10
print(f"bool(a):",bool(a))
print(f"bool(b):",bool(b))
print(f"bool(a) or bool(b) :",bool(a) or bool(b))

print("~"*20,f"Logical Operator OR. EX:3 ","~"*20)
a = 10
b = 0
print(f"bool(a):",bool(a))
print(f"bool(b):",bool(b))
print(f"bool(a) or bool(b) :",bool(a) or bool(b))

print("~"*20,f"Logical Operator OR. EX:4 ","~"*20)
a = 10
b = 10
print(f"bool(a):",bool(a))
print(f"bool(b):",bool(b))
print(f"bool(a) or bool(b) :",bool(a) or bool(b))

print("~"*20,f"Logical Operator NOT. EX:1 ","~"*20)
a = 10
print(f"bool(a):",bool(a))
print(f"Value of a = {a} , not {a} :", not a)


x,y,z = 204323,443456,546789
if x>y and x>z:
    print(f"X is the max value")
elif y>z and y>x:
    print(f"Y is the max value")
else:
    print(f"Z is the max value")

