import sys

file = open(r"C:\Users\Ridhaansh\PythonPractice\pythonProject1\Python_Practice\test.txt", 'w')
original = sys.stdout
sys.stdout = file

print("Hi Harry")
print("Where are you?", "Are you in bangalore!")
a = 10

print(a)
print("Value of a is: ", a)
b = 34
c = a + b
print(a, b, c)
print(a, b, c, sep=';')
print(a, b, c, sep=':')
print(a, b, c, sep='\t')
print(a, b, c, sep='\n')

source_cnt = 1000
target_count = 235
print(f"Source Count is {source_cnt}, "
      f"Target Count is {target_count} and Difference is {source_cnt - target_count}", end='\n')

print("_"*10)
f_count = source_cnt - target_count
print()

for i in range(1,f_count-750):
            print(i)

print("=" * 30, "Execution completed", "=" * 30)


