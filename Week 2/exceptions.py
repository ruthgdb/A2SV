t = int(input())
for i in range(t):
    a, b = input().split()
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
