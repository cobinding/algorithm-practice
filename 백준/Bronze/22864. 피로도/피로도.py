import sys; input=sys.stdin.readline

# 피로도쌓임, 한 일, 피로도감소, 번아웃
a, b, c, m = map(int, input().rsplit())
tired, to_do_work = 0, 0

for _ in range(24):
    if a > m : break
    # 일을 할 수 있는 상태
    if tired + a <= m :
        to_do_work += b
        tired += a
    # 쉬어야됨
    elif tired + a >= m :
        tired -= c
        if tired < 0 :
            tired = 0

print(to_do_work)