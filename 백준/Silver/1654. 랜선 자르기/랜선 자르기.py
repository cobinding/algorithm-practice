import sys;input=sys.stdin.readline

k,n=map(int,input().split())
lan=[int(input()) for _ in range(k)]

# 가장 짧은 길이를 1, 가장 긴 길이를 max(lan)으로 두고 이분 탐색한다.
left,right=1,max(lan)
ans=0
while left <= right:
    mid=(left+right)//2

    cnt_lan=0
    for item in lan:
        cnt_lan += item//mid

    if cnt_lan < n:
        right=mid-1
    elif cnt_lan >= n:
        left=mid+1
        ans=mid

print(ans)
