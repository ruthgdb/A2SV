def split_and_join(line):
    s = line.split(" ")
    s = "-".join(s)
    return s
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
