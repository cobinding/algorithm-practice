import sys; input=sys.stdin.readline

t = int(input())
tt = t
timer = [300, 60, 10]
timer_cnt = [0, 0, 0]

# 타이머 횟수 계산
for i in range(3):
    timer_cnt[i] = t // timer[i]
    t %= timer[i]

# T초를 맞출 수 있는지 확인
total_time = 0
for i in range(3):
    total_time += timer[i] * timer_cnt[i]


if total_time != tt :
    print(-1)
else:
    print(*timer_cnt)