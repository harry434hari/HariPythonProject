""" This Document is crated to practice on Identity operators
Created by Peddakotla Hari on 11/12/2024"""
""" Identity operators: we have 2 different types of membership operators
IS
IS NOT
Membership Operators: We have 2 different membership operators
IN 
NOT IN
"""

print("~"*20,f"Identity Operator IS: \n IS operator can be used to identity values are same for the 2 different valibles. EX:1 ","~"*20)
ls1 = [1,2,3]
ls2 = [1,2,3]
# Quick note: Memory allocation will be different for list
# values even the values are same for the different variables, Because list values are mutable
print(f"Memory allocation of ls1:",id(ls1))
print(f"Memory allocation of ls2:",id(ls2))
print(f"ls1 is ls2",ls1 is ls2)

print("~"*20,f"Identity Operator IS: \n IS operator can be used to identity values are same for the 2 different valibles. \n This example for tuple EX:1 ","~"*20)
tup1 = (1,2,3)
tup2 = (1,2,3)
# Quick note: Memory allocation will be same for tuple
#  values are unmutable
print(f"Memory allocation of tup1:",id(tup1))
print(f"Memory allocation of tup2:",id(tup2))
print(f"tup1 is tup2",tup1 is tup2)

print(f"IS NOT Operator will exactly opposite to IS Operator \n let's run same example from IS Operator for IS NOT")

ls1 = [1,2,3]
ls2 = [1,2,3]
print(f"Memory allocation of ls1:",id(ls1))
print(f"Memory allocation of ls2:",id(ls2))
print(f"ls1 is ls2",ls1 is not ls2)

tup1 = (1,2,3)
tup2 = (1,2,3)
print(f"Memory allocation of tup1:",id(tup1))
print(f"Memory allocation of tup2:",id(tup2))
print(f"tup1 is tup2",tup1 is not tup2)

