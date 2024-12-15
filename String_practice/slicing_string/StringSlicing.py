''' This Document is crated to practice String slicing
Created by Peddakotla Hari on 04/12/2024
Positive values practice'''

str = 'ETL Testing'

#Python index will start from 0
# Python index will end at -1
# To slice any iratative data(string, list, tuple, array, df etc) in python we have to use square brackets []
# sy

print(f"String slicing for {str} of str[0] is :",str[0])
print(f"String slicing for {str} of stg[-1] is :",str[-1])

print(f"test :",str[0],str[1],str[2],str[3],str[4],str[5],str[6],str[7],str[8],str[9],str[10])


# name split from email
# email is varible : which contains emails
#email[0] will help us to string start from 0 position
# find will help us to identify the search char
# step value = 1 means, print char by char, if 2 then 2 char by 2 char
# syntax: sequence[start:end:step]
# ex: str[0:4:1] 0 is start positon, 4 is end position , 1 is step : default value is 1 for step value

email = 'peddakotla.hari@gmail.com'

print(f"Email :", email)
f_name = email[0:email.find('.')]
ljunk_name = email[email.find('.')+1:]
L_Name = ljunk_name[0:ljunk_name.find('@')]
third = email[email.find('.')+1:]
d_name = third[third.find('@')+1:]
print('~'*22)
print(f"Separated_Names",'~'*22,f_name,L_Name,third,d_name,ljunk_name,sep='\n')
print('~'*22)
print()
print(f"third_stord:", third)
print('~'*10)

slicingstr = 'ETL Testing Automation'
# E T L   T e s t i n g     A   u   t   o   m   a   t   i   o   n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13  14  15  16  17  18  19  20  21

print(f"Slicing word for {slicingstr} of [2:10:1] :",slicingstr[2:20:4])
print(f"Slicing word for {slicingstr} of [2:10:1] :",slicingstr[1:13:6])
print(f"Slicing word for {slicingstr} of [2:10:1] :",slicingstr[1:7:8])
print(f"Slicing word for {slicingstr} of [2:10:1] :",slicingstr[1:7:4])


