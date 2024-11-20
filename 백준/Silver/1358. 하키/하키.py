import sys; input = sys.stdin.readline
# --------------------------------------------- #
# w, h : 직사각형 가로, 세로
# X, Y : 가장 왼쪽 아래 모서리
# R : h/2
# P : 선수의 수
# 선수들의 수가 주어질 때, 링크 안에 있는 선수의 수를 출력
# --------------------------------------------- #

# 점과 점사이의 거리
def cal_dist(x, y, a, b):
    dist = ((x-a)**2 + (y-b)**2) ** (1/2)
    r = h//2
    if dist <= r :return True
    else: return False

w,h,lx,ly,p = map(int, input().split())

cnt = 0
for _ in range(p):
    x, y = map(int, input().split())

    # 사각형 안 확인
    if (lx <= x <= lx+w) and (ly <= y <= ly+h):
        cnt += 1

    # 왼쪽 반원 확인
    elif cal_dist(lx, ly+h//2, x, y):
        cnt += 1

    # 오른쪽 반원 확인
    elif cal_dist(lx+w, ly+h//2, x, y):
        cnt += 1

print(cnt)