import sys; input=sys.stdin.readline
from collections import deque

t = int(input())

def no_conv(festival_yx):
    if abs(home_y-festival_yx[0]) + abs(home_x-festival_yx[1]) <= 1000:
        return "happy"
    else:
        return "sad"


def solve(conv_yx, festival_yx):
    visited = [False for _ in range(conv_n)]
    q = deque()
    q.append((home_y, home_x))

    while q:
        y, x = q.popleft()
        if abs(festival_yx[0] - y) + abs(festival_yx[1] - x) <= 1000:
            return "happy"

        for i in range(conv_n):
            if visited[i]: continue
            if abs(conv_yx[i][0] - y) + abs(conv_yx[i][1] - x) > 1000 : continue

            q.append((conv_yx[i][0], conv_yx[i][1]))
            visited[i] = True

    return "sad"

for _ in range(t):
    conv_n = int(input())
    home_y, home_x = map(int, input().split())

    # 편의점 개수가 0개일 때는 바로 페스티벌과의 거리 계산
    if conv_n == 0:
        festival_yx = list(map(int, input().split()))
        result = no_conv(festival_yx)
        print(result)

    # 아닐 때는 그래프 탐색
    else:
        conv_yx = [list(map(int, input().split())) for _ in range(conv_n)]
        festival_yx = list(map(int, input().split()))

        result = solve(conv_yx, festival_yx)
        print(result)