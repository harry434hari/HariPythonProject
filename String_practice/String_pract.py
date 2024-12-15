''' This Document is crated to practice String data type
Created by Peddakotla Hari on 02/12/2024'''


string = 'ETL Testing'

print("String value :",string)
print("Datatype of String",type(string))
print("Memory allocation of string :",id(string))

print("="*100)

string11 = 'BIG DATA TESTING'
print(f"lower string {string11} :",string11.lower())
print(f"Swapcase {string11}:",string11.swapcase())
print(f"T count in {string11}:",string11.count('T'))
print(f"It's just trail to check the char count by hari for {string11}",string11.count(string11))

print()

print(f"T Count in {string11} = ",string11.count('T'), f"A count in {string11} = ",string11.count('A'))

print()

stringstart = 'starts with'
print(f"Starts with testing {stringstart}",stringstart.startswith('s'))
print()
string15 = 'ends with'
print(f"ends with testing {string15}",string15.endswith('h'))
print()

str9 = input("Enter the input value : ")
print("str9.find('Test')",str9.find('Test'))

print("="* 100)

isalpha = input("Enter the values to check isalpha :")
print(f"{isalpha}",isalpha.isalpha())

isnumaric = input("Enter the value :")
print(f"{isnumaric} is ",isnumaric.isalnum())

junk_data = input("Enter the non ascii value :") # ex: é, à, ö, ñ, et
print(f"Enter the junk data",junk_data.isascii())

