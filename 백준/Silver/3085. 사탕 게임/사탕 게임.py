import sys;input=sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def check():
    # 3-1. 가장 긴 행 확인
    ans_row = 1
    for i in range(n):
        cnt_row = 1
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                cnt_row += 1
            else:
                cnt_row = 1

            # 최댓값 확인
            if cnt_row > ans_row :
                ans_row = cnt_row

    # 3-2. 가장 긴 열 확인
    ans_col = 1
    for i in range(n):
        cnt_col = 1
        for j in range(n-1):
            if graph[j][i] == graph[j+1][i]:
                cnt_col += 1
            else:
                cnt_col = 1

            # 최댓값 확인
            if cnt_col > ans_col :
                ans_col = cnt_col

    return max(ans_col, ans_row)

# 1. 색이 다른 인접 칸 찾기
ans = 0
for y in range(n):
    for x in range(n):
        # 인접 지역 탐색
        for dy, dx in d :
            ny, nx = y+dy, x+dx
            # 2. 인접 칸 사탕 교체
            if 0 <= ny < n and 0 <= nx < n:
                if graph[y][x] != graph[ny][nx]:
                    # swap([y][x],[ny][nx])
                    graph[ny][nx], graph[y][x] = graph[y][x], graph[ny][nx]

                    # 최대 행/열 찾기
                    tmp = check()
                    ans = max(ans, tmp)

                    # swap 했던 것 원위치로
                    graph[ny][nx], graph[y][x] = graph[y][x], graph[ny][nx]

print(ans)