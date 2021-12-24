n = int(input())
result = set(map(int, input().split()))
N = int(input())
for i in range(N):
    commands = list(input().split())
    if commands[0] == "discard":
        result.discard(int(commands[1]))
    elif commands[0] == "remove":
        result.remove(int(commands[1]))
    elif commands[0] == "pop":
        result.pop()
print(sum(result))
