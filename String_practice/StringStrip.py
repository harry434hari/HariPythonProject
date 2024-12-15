''' This Document is crated to practice String Strip
Created by Peddakotla Hari on 03/12/2024'''

# str = input("Enter Full name :")
# print(f"Full Name :",str.strip())
# print(f"length before strip apply :",len(str))
# print(f"length after strip apply :",len(str.strip()))

str1 = input("Enter the work with any special char at start and end :")
clean_data = str1.strip('#')
print(clean_data.upper())

