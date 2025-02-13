import sys;input=sys.stdin.readline

# 1. 값을 [0] + 입력으로 받아서 인덱스가 1부터 시작하도록
n,k = map(int, input().split())
li = [i for i in range(1, n+1)]

# 2. 인덱스 값을 (idx+k)%k
idx = 0
res = []
for _ in range(n):
    # 요세푸스 순열 규칙으로 리스트를 순회하기 위한 인덱스 점화식
    idx += (k-1)
    idx %= len(li)

    # 요세푸스에 따른 새로운 순열 생성
    res.append(str(li[idx]))
    li.pop(idx)

print("<", ', '.join(res), ">", sep="")