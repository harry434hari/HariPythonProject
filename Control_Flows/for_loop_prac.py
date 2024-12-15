""" This Document is crated to practice on For loop
Created by Peddakotla Hari on 12/13/2024"""

# Syntax : for loop
# for element in collection data type/ string data types
# code

ls = [1, 2, 3, 4]
for element in ls:
    print("@" * element)

ls1 = ('RIDHAANSH')
for element in ls1:
    print(f"Char in element is {element}")

dict = {201: 'Ridhaansh', 202: 'Raghavendra', 203: 'Manjunath'}

ls = [6]
for element in ls:
    print("~~~~~" * element)

for i, j in dict.items():
    print(i, j)

ls = [6]
for element in ls:
    print("~~~~~" * element)

for i in dict.keys():
    print(f"Keys :", i)

ls = [6]
for element in ls:
    print("~~~~~" * element)

for j in dict.values():
    print(f"Values : ", j)

ls = [6]
for element in ls:
    print("~~~~~" * element)

for key, value in dict.items():
    print(f"Key is {key} and value is {value}")

ls = [6]
for element in ls:
    print("~~~~~~~~~~~~~~" * element)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in num:
    print(i * i)

ls = [6]
for element in ls:
    print("~~~~~~~~~~~~~~" * element)

ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls_even = []
ls_odd = []
for i in ls2:
    # print(f"i value is ",i)
    if i % 2 == 0:
        print(i, "is even number")
        ls_even.append(i)
    else:
        print(i, "is odd number")
        ls_odd.append(i)

print(f"Even numbers :", ls_even)
print(f"Odd numbers :", ls_odd)

ls = [6]
for element in ls:
    print("~~~~~~~~~~~~~~" * element)

age = range(1, 30)
eligible_count = 0
not_eligible_count = 0
for i in age:
    # print(i)
    if i >= 18:
        print(i, "is eligible to vote")
        eligible_count = eligible_count + 1

    else:
        print(i, "is eligible to vote after", abs(i - 18), "Year")
        not_eligible_count = not_eligible_count + 1

print(f"eligible_count :", eligible_count)
print(f"not_eligible_count :", not_eligible_count)

ls = [6]
for element in ls:
    print("~~~~~~~~~~~~~~" * element)

# add sum of 1 to given number
# ad = int(input("Enter any number :"))
# sum = 0
# in_value = range(1,ad+1)
# for i in in_value:
#    # print(i)
#     sum = sum+i
# print(f"Sum of 1 to {ad} is :", sum)
#
# # the above code can be replaced with below code in 1 line
# print(sum(range(1,ad+1)))
#
# # the above code can be replaced with below code in 1 line
# n = int(input("Enter value n*(n+1)/2: "))
# sum2 = n*(n+1)/2
# print(sum2)

# Write a code to sum of given sen numbers

ls3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_even = 0
sum_odd = 0
even_values = []
odd_values = []
for i in ls3:
    #print(f"i value is ",i)
    if i % 2 == 0:
        print(i, "is even number")
        even_values.append()
    else:
        print(i, "is odd number")
        odd_values.append()

print("even_values :", even_values)
print("odd_values :", odd_values)

#----------------------------------------------------------------



ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls_even = []
ls_odd = []
for i in ls2:
    # print(f"i value is ",i)
    if i % 2 == 0:
        print(i, "is even number")
        ls_even.append(i)
    else:
        print(i, "is odd number")
        ls_odd.append(i)

print("ls_even :", ls_even)
print("ls_odd :", ls_odd)

print("Sum Of ls_even: ",sum(ls_even))
print("Sum Of ls_odd: ",sum(ls_odd))

#---------------------------------------


ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls_even = []
ls_odd = []
for i in ls2:
    # print(f"i value is ",i)
    if i % 2 == 0:
        print(i, "is even number")
        ls_even.append(i)
    else:
        print(i, "is odd number")
        ls_odd.append(i)

print("ls_even :", ls_even)
print("ls_odd :", ls_odd)

print("Sum Of ls_even: ",sum(ls_even))
print("Sum Of ls_odd: ",sum(ls_odd))
