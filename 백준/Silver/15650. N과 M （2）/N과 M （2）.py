n,m = map(int, input().split())

arr = list(range(1,n+1))
comb = []

def combination(start, curr_num):
    if curr_num == m:
        print(*comb)
        return

    # 나(start)부터 끝까지 탐색 - 이전 거에는 관심 X
    for i in range(start, len(arr)):
        comb.append(arr[i])
        combination(i+1, curr_num+1)
        comb.pop()

combination(0,0)