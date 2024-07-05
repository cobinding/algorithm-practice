import sys;input=sys.stdin.readline

n,m=map(int,input().split())
arr=sorted(int(input()) for _ in range(n))

min_sub=sys.maxsize
left,right=0,0

# 포인터 2개 준비, 같이 전진하는 형식으로 O(N)을 넘지 않게 구현한다.
while left < n and right < n:
    tmp=arr[right]-arr[left]
    
    if tmp >= m:
        min_sub=min(min_sub, arr[right]-arr[left])
        left += 1
    
    # 차이가 m보다 작은 경우 큰 수를 포인팅해서 찾아나감
    else:
        right += 1
    
print(min_sub)