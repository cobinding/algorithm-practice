import sys
input = sys.stdin.readline
t = int(input())

# 백트래킹 함수
def back(total):
    global response
    
    # 재귀 return 조건
    if sum(total) == n:
        response += 1
        return
        
    for num in range(1,4):
        if not total or sum(total) + num <= n :
            total.append(num)
            back(total)
            total.pop()
    
for _ in range(t):
    n = int(input())
    total = []
    response = 0
    back(total)
    print(response)