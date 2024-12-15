""" This madule is created to practice int datatype
Created by Peddakotla Hari on 28/12/2024"""

""" 
Definitation: Interger is a numaric data type and it will store numaric data only
it's defined as int: ex: 1,2,3,-1,-2 
1. In interger we have n number of methods 
    most of the time we use 
    __abs__ to covert negative values into positive values
    __add__ to do sum on values

Note: to display available methods on any of the data types use below script
    
    print("TO display avalable interger methods",dir(Interger varable name))
    ex: 
            #a = 100
            #print("Methods of int",dir(a))

"""

count = 10

print("Value of count is", count)
print("Data type of count is",type(count))
print("Memory location for count is",id(count))

""" Look at Memory allocation values for above count and below count2 values,
Both address locations are same because, since the stored values are same for both varibles(count & count2)
 python will not store saparatly for same values. So it will refer erilier address only
 
 For every run memory allocation will be changing but same set of values memory allocation will be same"""

count2 = 10
print("Value of count2 is",count2)
print("Data type of count2 is", type(count2))
print("Memory allocation for count2 is",id(count2))

count3 = 14
print("value of count3 is",count3)
print("Data type for count3 is",type(count3))
print("Memory allocation of count3",id(count3))

count6 = -18
print("value of count6 is",count6)
print("Data type for count6 is",type(count6))
print("Memory allocation of count6",id(count6))

print("Absulute value of count3",count3.__abs__())

print("Absulute value of count6",count6.__abs__())

count8 = -10

print(f"Method of addition for {count} and {count8}",count8.__add__(count))

#a = 100
#print("Methods of int",dir(a))

count_float = 19.33
print("Value of float data type value for count_float",count_float)
print("Type of float count_float",type(count_float))
print("Memory allocation for count_Float",id(count_float))

print("Methods of float data type for count_float",dir(count_float))

long_float = 11.1

print("ceil value of long_float",long_float.__ceil__())

#~~~~~~~~~~~~~~~
z = 10
y = 20

w = y - z
print(w)
