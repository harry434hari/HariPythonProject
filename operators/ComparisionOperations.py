""" This Document is crated to practice on Comparison Operators or Relational operators
Created by Peddakotla Hari on 11/12/2024"""

# 5==5 "==" is comparison operator
print("~"*10,f"a==b","~"*10)
a = 10
b = 10.1
print(f"a==b :", a==b)

print("~"*10,f"a==b :","~"*10)
a = 10
b = 10
print(f"a==b :", a==b)

print("~"*10,f"a!=b :","~"*10)
a = 10
b = 10.1
print(f"a!=b :", a!=b)

print("~"*10,f"a>b:","~"*10)
a = 10
b = 10.1
print(f"a>b :", a>b)

print("~"*10,f"a<b:","~"*10)
a = 10
b = 10.1
print(f"a<b :", a<b)

print("~"*10,f"a<=b:","~"*10)
a = 10
b = 10.1
print(f"a<=b :", a <= b)

print("~"*10,f"a>=b:","~"*10)
a = 10
b = 10.1
print(f"a>=b :", a >= b)

print("~"*20,f"Let's try with ETL Scenario use case for count matching","~"*20)
source_count = 10
Target_count = 10
if source_count == Target_count:
    print(f"Count is matching and test case PASS")
else:
    print(f"Count is not matching and count difference is =",source_count-Target_count)

print("~"*20,f"Let's try with ETL Scenario use case for miss match records","~"*20)
source_count = 10
Target_count = 8
if source_count == Target_count:
    print(f"Count is matching and test case PASS")
else:
    print(f"Count is not matching and count difference is =",source_count-Target_count)

print("~"*20,f"Age eligibility to check vote","~"*20)
#age = 18
age = int(input(f"Enter your age:"))
if age >= 18:
    print(f"You are eligible to vote")
else:
    print(f"You are not eligible to vote")
