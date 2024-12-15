''' This Document is crated to practice String slicing
Created by Peddakotla Hari on 04/12/2024
negative values practice'''

Ne_slicing = 'ETL Testing Automation'
print(Ne_slicing)
print(f"Negative slicing values practice for [-1:-4:-4] :",Ne_slicing[-1])
print(Ne_slicing[-2])
print(Ne_slicing[-3])
print(Ne_slicing[0:-9])
print(Ne_slicing[0:9])
print(Ne_slicing[1:-16:3])
print(f"Both negative values[-6:-1]:",Ne_slicing[-6:-1])

slicingstr = 'ETL Testing Automation'
#  E    T    L         T   e    s   t   i   n   g       A  u  t  o  m  a  t  i  o  n
# -22 -21  -20  -19  -18  -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(Ne_slicing[-12:-7:1])
# start value is => -12
# end value is => -7-1 = -8
# step value is +1
# Output will start printing from -12 to -8 with 1 step from Right to left i.e : g Aut

print(f"[-21:-3:3] :",Ne_slicing[-21:-3:3])
#op: TTtgum

print(f"[-21:-1:-4]: ",Ne_slicing[-21:-1:1])
print(Ne_slicing[-1:5:-1])

print(f"[::-1] :",Ne_slicing[::-1])

print(f"[::-2] :",Ne_slicing[::-2])

print(f"[::-3] :",Ne_slicing[::-3])