"""
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

# ~~~~~~~~~~~Tables for any value~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = int(input("Enter the value :"))

for i in num1:
    print(f"{num2} * {i} =", num2 * i)
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

num3 = int(input("Enter the value :"))
num4 = 1
for i in range(1,num3+1):
    num4 *= i
    print(num4)


