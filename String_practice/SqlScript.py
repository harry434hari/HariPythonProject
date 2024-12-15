
'''env = ['DEV','SQA','UAT','PROD']
table = ['EMP','DEP','LOC','SALES']

for i in env:
    for j in table:
        print(f"select * from {i}.{j}")'''

print()

schema = input("Enter schema name :")
table = input("Enter table name :")
age = input("Enter age :")
second_table = input("Enter second table name :")
pk_column = input("Enter PK column name :")

query = f"""Select * from {schema}.{table} a Inner join {schema}.{second_table} b 
         on a.{pk_column} = b.{pk_column} where a.age>{age};"""
print(query)
