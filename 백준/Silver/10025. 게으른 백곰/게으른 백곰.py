import sys;input=sys.stdin.readline

n,k=map(int,input().split())

arr=[0 for _ in range(1000000)]
min_max_idx=[]
for _ in range(n):
    gram,x_coord=map(int,input().split())
    arr[x_coord]=gram
    min_max_idx.append(x_coord)

# 좌표의 첫시작과 끝지점
start,end=min(min_max_idx),max(min_max_idx)

# 윈도우 범위 - 양 끝도 포함이므로 [x-k,x+k]의 거리
window_size=2*k+1

# k까지의 가장 최근 합
current_sum=sum(arr[:window_size])
max_sum=current_sum

# 현재 합을 누적하면서 구하기 위해서 가장 오른쪽은 더하고, 가장 왼쪽 값은 뻬주면서 슬라이딩
for i in range(window_size, end+1):
    # 현재 위치 i는 더해나가면서, window 맨 앞의 값은 빼줌
    current_sum += (arr[i]-arr[i-window_size])
    max_sum=max(current_sum,max_sum)

print(max_sum)