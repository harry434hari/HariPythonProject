print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
print(type(10))
print(type({}) is dict)

x = 50
def fun1():
    x = 25
    print(x)
fun1()
print(x)

print(type(range(5)))