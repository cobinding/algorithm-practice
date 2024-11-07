import sys;input=sys.stdin.readline

n,m = map(int, input().split())
arr = [sorted(map(int, input().split()), reverse=True) for _ in range(n)]

# 각 턴을 비교하기 위해 arr transport
trans = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(arr[j][i])
    trans.append(tmp)

# transport arr를 돌면서 매 턴마다 max값 확인
# max_card와 같거나 크다면 승리 처리
d = dict()
for i in range(len(trans)):
    max_card = max(trans[i])
    for j in range(len(trans[i])):
        if trans[i][j] >= max_card:
            if not d.get(j+1):
                d[j+1] = 1
            else:
                d[j+1] += 1

ans = []
for k, v in d.items():
    winner = max(list(d.values()))
    if v == winner:
        ans.append(k)

print(*sorted(ans))