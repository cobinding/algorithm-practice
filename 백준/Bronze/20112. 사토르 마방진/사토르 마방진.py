import sys; input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

flag = True
for i in range(n):
    for j in range(n):
        # 한 번이라도 달라지면 False / break
        if words[i][j] != words[j][i]:
            flag = False
            break

print('YES') if flag else print('NO')