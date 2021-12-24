def swap_case(s):
    a = ""
    for x in s:
        if x.isupper():
            a = a + x.lower()
        else:
            a = a + x.upper()
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)