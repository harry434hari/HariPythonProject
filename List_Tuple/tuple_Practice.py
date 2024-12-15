''' This Document is crated to practice on list tuple data type
Created by Peddakotla Hari on 06/12/2024

List_Tuple is a collection datatypes, it will store multiple data types.

syntax: list_tuple = [1,3,-1,'Hello',1+2j,(10,1996),[5,2022],True]'''
import sys

list_tuple = [1,3,-1,'Hello',1+2j,(10,1996),[5,2022],True]
print(f"list_tuple value :",list_tuple)
print(f"list_tuple data type :",type(list_tuple))
print(f"Memory allocation of list_tuple :",id(list_tuple))
print("~"*30,'Char wise display with help of slice values',"~"*30)
print(f"Char wise display with help of slice values[0] :",list_tuple[0])
print(f"Char wise display with help of slice values[1] :",list_tuple[1])
print(f"Char wise display with help of slice values[2] :",list_tuple[2])
print(f"Char wise display with help of slice values[3] :",list_tuple[3])
print(f"Char wise display with help of slice values[4] :",list_tuple[4])
print(f"Char wise display with help of slice values[6] :",list_tuple[5])
print(f"Char wise display with help of slice values[6] :",list_tuple[6])
print(f"Char wise display with help of slice values[7] :",list_tuple[7])
print("~"*30,'To display data types for inside list values',"~"*30)
print(f"Char wise display with help of slice values[0] :",list_tuple[0],type(list_tuple[0]))
print(f"Char wise display with help of slice values[1] :",list_tuple[1],type(list_tuple[1]))
print(f"Char wise display with help of slice values[2] :",list_tuple[2],type(list_tuple[2]))
print(f"Char wise display with help of slice values[3] :",list_tuple[3],type(list_tuple[3]))
print(f"Char wise display with help of slice values[4] :",list_tuple[4],type(list_tuple[4]))
print(f"Char wise display with help of slice values[5] :",list_tuple[5],type(list_tuple[5]))
print(f"Char wise display with help of slice values[6] :",list_tuple[6],type(list_tuple[6]))
print(f"Char wise display with help of slice values[7] :",list_tuple[7],type(list_tuple[7]))
print("~"*30,'To display address allocation for each values',"~"*30)
print(f"Char wise display with help of slice values[0] :",list_tuple[0],id(list_tuple[0]))
print(f"Char wise display with help of slice values[1] :",list_tuple[1],id(list_tuple[1]))
print(f"Char wise display with help of slice values[2] :",list_tuple[2],id(list_tuple[2]))
print(f"Char wise display with help of slice values[3] :",list_tuple[3],id(list_tuple[3]))
print(f"Char wise display with help of slice values[4] :",list_tuple[4],id(list_tuple[4]))
print(f"Char wise display with help of slice values[5] :",list_tuple[5],id(list_tuple[5]))
print(f"Char wise display with help of slice values[6] :",list_tuple[6],id(list_tuple[6]))
print(f"Char wise display with help of slice values[7] :",list_tuple[7],id(list_tuple[7]))

ls1 = []
print(f"[] value:",ls1)
print(f"[] type:",type(ls1))
print(f"[] id:",id(ls1))

ls2 = list()
print(f"[] value:",ls2)
print(f"[] type:",type(ls2))
print(f"[] id:",id(ls2))

print(dir(ls2))
print("~"*30,'Practicing append',"~"*30)
# after append
ls2.append(5)
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print("~"*10,'Appending again to check the how the next value will be added into list',"~"*10)
ls2.append(6)
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print(f"It's adding second input value at the end of the list by default")
print()
print("~"*10,'Appending 3rd time to check the how the next value will be added into list',"~"*10)
ls2.append(7)
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print(f"==> It's clear that, append will load every new entry at end of the list")
print()
print("~"*10,f"Now let's try with INSERT Method, "
      f"It will have slice values to store the values into specific location","~"*10,)
ls2.insert(2,9)
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print("~"*10,f"Lets try with same index values for the different value"
             f"is this going to be assign privious value to the next index or not ?"
             f"Ex: prious data is [5, 6, 9, 7] "
             f"Now : we are tring [5, 6,{2,8} to (9), 7] ","~"*10,)
ls2.insert(2,8)
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print(f"As we expected privious index value is agigned to new value and it's shifter to next index for prious value")
ls2.append([1.2,2.2])
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print("~"*10,'Extend practice: it can be used for multiple values insert at a time',"~"*10)
ls2.extend('Hari')
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print("~"*10,'Extend practice: with numbers',"~"*10)
ls2.extend((0.7,0.8,0.6,0.5,9,9,9,9))
print(f"ls2 value:",ls2)
print(f"ls2 type:",type(ls2))
print(f"ls2 id:",id(ls2))
print(ls2)
print(f"Count of 9 in ls2 :",ls2.count(9))
print(f"Count of H in ls2 :",ls2.count('H'))
print()
# to copy from one varible to other varible we have to use copy() like below
ls3 = ls2.copy()
print(f"ls3:",ls3)
print(f"ls2:",ls2)
print("~"*10,'pop method to remove values from any of the list',"~"*10)
# pop will take index to remove values from list,
# ex : 9 is the index of 'i' from ls2 and it will remove i value from ls2
ls2.pop(9)
print(f"After pop apply on ls2 to remove 9")
print(f"ls2:",ls2)
print(f"ls3:",ls3)
ls2.pop(0) # 0 is index, now it will remove 5 value from ls2
print(f"After pop 0 index will apply on ls2 to remove 5")
print(f"ls2:",ls2)
print(f"ls3:",ls3)

# remove method will help us to remove value from the list
ls2.remove(9)
print(f"After remove 9 value from ls2")
print(f"ls2:",ls2)
print(f"ls3:",ls3)
ls2.remove(0.6)
print(f"After remove 0.6 value from ls2")
print(f"ls2:",ls2)
print(f"ls3:",ls3)
print()
ls2.clear()
print(f"To clear all values from the ls2:",ls2)
print(f"ls2:",ls2)
print(f"ls3:",ls3)
print(f"Before Revers ls3:",ls3,ls3.reverse())
print("After Revers ls3:",ls3.reverse())

ls5 = [33,'ETL Testing',1,0.3]
ls5.reverse()
print(f"After revers ls5")
print(ls5)

# feature           List                         Tuple
# Mutabulity    We can modify, add,delete.      We can't modify
# Syntax        []                              ()
# Memory        Less memory efficent, slower.   More memory efficent, faster
# Usage         Sutable for dynamic collection. Sutable for static collications

ls = [1,2,3,4]
tu = (1,2,3,4)

print(f"Size of list :",sys.getsizeof(ls))
print(f"Size of Tuple :",sys.getsizeof(tu))

lse = []
tue = ()

print(f"Size of Empty list :",sys.getsizeof(lse))
print(f"Size of Empty Tuple :",sys.getsizeof(tue))

# Conversion data types

lis = [1,2,3]
tup = (1,2,3)
print(f"lis data type before conversion :",type(lis))
print(f"tup data type before conversion :",type(tup))
lis = tuple(lis)
tup = list(tup)
print(f"lis data type After conversion :",type(lis))
print(f"Tup data type After conversion :",type(tup))