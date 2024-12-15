""" This Document is crated to practice on Assignment Operators
Created by Peddakotla Hari on 8/12/2024"""

c = 10
a = b = c = 10
a,b,c = 10,10,10
a,b,c = 10,11,12

print(f"a :", a)
print(f"b :", b)
print(f"c :", c)

m = 20
print(f"m value before Assignment operation:", m)
m = m + 3
print(f"m value after Assignment Operation :",m)

n = 15.5
print(f"Before Assign operation:", n)
n = n * 44.6
print(f"After Assign operation:", n)

p = 100
print(f"Before Assign operation :", p)
p-= 33
print(f"After Assign operation p-=33 :", p)

q,r = ('Hari'),['Ridhu']
print(f"Q value :",q)
print(f"R value :",r)


x = 102
print(f"X value :",x)
x/= 4
print(f"X value X/= 4 :",x)

x = 102
print(f"X value :",x)
x//= 4
print(f"X value X//= 4 :",x)


i = 2
print(f"i value :",i)
#i = i **3
i **=3
print(f"X value i = i **3:",i)


