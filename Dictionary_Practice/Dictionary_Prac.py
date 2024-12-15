""" This Document is crated to practice on Dictionary
Created by Peddakotla Hari on 07/12/2024"""
import sys

lse = []
tue = ()
d = {}
print(f"Value of d:", d)
print(f"Type of dict :", type(d))
print(f"Size of Empty Dict :", sys.getsizeof(d))
print(f"Size of Empty list :", sys.getsizeof(lse))
print(f"Size of Empty Tuple :", sys.getsizeof(tue))
print(f"Methods available in Dict :", dir(d))

 # d[Key] = value
 # d = {key: Value, Key2: Value, ....}
d[0] = ('Hari')
d[1] = ('Ravi')
print(f"Values of d :",d)
print()
print(f"~~~~Lets update d key with some additional values~~~~")
d.update({2:'Manju'})
print(f"After Updating d:", d)
d.update({3:'Naga',5:'Kamesh'})
print(f"After updating some more key and values :",d)
d.update({1:'Ridhaansh',4:'Basha'})
print(f"Updating new value for old value for Key value 1 :",d)
print(d)
print(f"d.get(1),len(d.get(1)) :",d.get(1),": length :",len(d.get(1)))
print(f"d.get(2),len(d.get(2)) :",d.get(2),": length :",len(d.get(2)))
print(f"d.get(3),len(d.get(3)) :",d.get(3),": length :",len(d.get(3)))
print(f"d.get(4),len(d.get(4)) :",d.get(4),": length :",len(d.get(4)))
print(f"d.get(5),len(d.get(5)) :",d.get(5),": length :",len(d.get(5)))
print()
print(f"TO display number of keys in the Dict, we can use KEY Method :", d.keys())
print(f"TO display values in the Dict, we can use values Method :", d.values())
print(f"TO remove last eliement of the dict, we can use POPITEM method: ",d.popitem())
print(d)
print(f"to remove any specific value from the Dict we can use pop :",d.pop(3))
print(f"After removing key 3 then actual values in Dict :", d)
print()
print(f"~"*30,"Set operators","~"*30)
sets = {9,4,6,2,6,7,1,3,2,4,8,4,6,8,1,0}
dict = {'Name':'Hari', 'Collage':'ABC'}
print(f"In the sets we have given values randamally and \n some of the values are repeted, means we have given duplicates.\n SET : have property to display in the order format and uniqu data set, \n Check the below results and input values from the set. \n ==> To create empty set we have use set(), \n Basically when we are adding some values into set directly then we can use set{1,54,3,5,6,345}")
print(f"Type of sets :", type(sets))
print(f"Type of Dict :", type(dict))
print(f"Values of sets :", sets)
print(f"Values of Dict :", dict)

s = {}
s2 = set()
print(f"Type of s :", type(s))
print(f"Type of s2 :", type(s2))
print(f"size of s :",sys.getsizeof(s))
print(f"size of s2 :",sys.getsizeof(s2))
print(sets)
print(f"Lets try adding some strings into sets")
sets.add("Ridhaansh")
print(f"After adding string value into SETS :",sets)
sets.add("Jyothi")
print(f"After adding string value into SETS :",sets)
sets.update('Harry')
print(f"After Updating string value into SETS :",sets)
sets.update('sreeni')
print(f"After Updating string value into SETS :",sets)

sets.remove(9)
print(f"Applying REMOVE method for 9 int :",sets)

# REMOVE method will remove any specified values
# DISCARD method also will perform same operation as REMOVE method
# But the difference is, If we try to REMOVE any values(Which are not present in the SET then it will through runn time error)
# But in the DISCARD method, it will not through any error, it will run without any error.

# sets.remove(9)
# print(f"Applying REMOVE method for 9 int :",sets)

sets.discard(9)
print(f"Applying DISCARD method for 9 int :",sets)
sets.discard('H')
print(f"Applying DISCARD method for H :",sets)

# Just a quick note, POP method will remove any eliment when we apply,
# we don't have any control which element to remove.

