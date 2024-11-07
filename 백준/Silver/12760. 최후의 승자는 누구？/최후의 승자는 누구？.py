import sys;input=sys.stdin.readline

n,m = map(int, input().split())
cards = [sorted(map(int, input().split()), reverse=True) for _ in range(n)]
score = [0 for _ in range(n)]

for i in range(m):
    max_val = 0
    for j in range(n):
        max_val = max(max_val, cards[j][i])
    for j in range(n):
        if cards[j][i] == max_val:
            score[j] += 1

max_score = max(score)
for i in range(n):
    if score[i] == max_score:
        print(i+1, end = ' ')