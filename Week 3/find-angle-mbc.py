import math

A = int(input())
B = int(input())
x = math.atan2(A,B)
x = round(math.degrees(x))
print(x,chr(176),sep="")