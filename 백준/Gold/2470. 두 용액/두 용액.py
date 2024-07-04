import sys;input=sys.stdin.readline

n=int(input())
arr=sorted(map(int,input().split()))

start,end=0,n-1
ans_start, ans_end=0,0
target=10000000000

while start < end and start >= 0:
    
    tmp=arr[start]+arr[end]
    if tmp==0:
        ans_start,ans_end=start,end
        break
    
    # min(abs(tmp), target)
    # 두 수의 합이 최소인 경우를 루프가 돌 때마다 확인 및 갱신
    if abs(tmp)<target:
        ans_start,ans_end=start,end
        target=abs(tmp)

    # 두 수의 합이 0보다 크면 끝 포인터를 한 칸 앞으로 옮겨서, 수 줄이기
    if tmp > 0:
        end -= 1
    
    # 두 수의 합이 0보다 작으면 시작 포인터를 한 칸 뒤로 옮겨서, 수 늘리기
    elif tmp < 0:
        start += 1


print(arr[ans_start], arr[ans_end]) 