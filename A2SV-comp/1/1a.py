n = 5
x = 1
for i in range(n):
  print("-"*(n-i),end="")
  print("*"*x,end="")
  x += 2
  print()