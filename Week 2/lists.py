if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        commands = list(input().split())
        if commands[0] == "insert":
            result.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == "print":
            print(result)
        elif commands[0] == "remove":
            el = int(commands[1])
            result.remove(el)
        elif commands[0] == "append":
            result.append(int(commands[1]))
        elif commands[0] == "sort":
            result.sort()
        elif commands[0] == "pop":
            result.pop()
        elif commands[0] == "reverse":
            result.reverse()
    
