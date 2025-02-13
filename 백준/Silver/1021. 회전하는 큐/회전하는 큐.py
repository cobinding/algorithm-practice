import sys;input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
position = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])

cnt = 0
i = 0
target_cnt = 0
while True:
    # 다 찾을 때까지 반복: O(NM) = 2500
    if target_cnt == len(position):
        break

    target = position[i]

    # 항상 첫 번째에 와야 제거 가능
    if queue[0] == target:  # O(N)
        queue.popleft()
        target_cnt += 1
        i += 1

    # 인덱스가 중간값보다 뒤에 있는 경우
    # 오른쪽 이동으로 이동 최소화
    elif queue.index(target) > len(queue)//2:
        queue.rotate(1)
        cnt += 1

    elif queue.index(target) <= len(queue)//2:
        queue.rotate(-1)
        cnt += 1

print(cnt)