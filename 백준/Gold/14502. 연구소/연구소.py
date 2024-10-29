from collections import deque
import sys; input = sys.stdin.readline
import copy

n, m = map(int, input().split())  # 행, 열
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
d = [(-1,0),(1,0),(0,1),(0,-1)]


# 백트래킹으로 모든 case에 대해 벽을 설치해서 BFS 탐색
def createWall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                graph[y][x] = 1
                createWall(wall_cnt + 1)
                graph[y][x] = 0

def bfs():
    global result
    copy_graph = copy.deepcopy(graph)
    q = deque()

    # 바이러스 위치 정보 저장
    for y in range(n):
        for x in range(m):
            if copy_graph[y][x] == 2:
                q.append((y, x))

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny, nx = y+dy, x+dx

            if 0 <= ny < n and 0 <= nx < m and copy_graph[ny][nx] == 0:
                copy_graph[ny][nx] = 2
                q.append((ny, nx))

    safezone = 0
    for item in copy_graph:
        safezone += item.count(0)

    result = max(safezone, result)

createWall(0)
print(result)