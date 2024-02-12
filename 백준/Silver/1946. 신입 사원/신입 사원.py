import sys;input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    score = [list(map(int,input().split())) for _ in range(n)]
    score = sorted(score, key = lambda x:(x[0],x[1]))

    first = score[0][1]
    cnt = 1
    for i in range(1, n):
        if first > score[i][1] :
            cnt += 1
            first = score[i][1]
        
    print(cnt)