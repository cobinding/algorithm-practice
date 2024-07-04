n,s=map(int,input().split())
arr=list(map(int,input().split()))

left,right=0,0
target=0
section=100000 # n은 1과 100,000 사이이므로 구간의 최대 길이는 100,000

while True:
    target+=arr[right]

    while target>=s:
        # 가장 짧은 구간은?
        section=min(right-left+1, section)
        
        # left pointer 조작을 통해 구간합 탐색
        target-=arr[left]
        left+=1

    # 끝까지 모두 탐색한 경우
    if right == n-1:
        break
    
    right += 1

print(0) if section==100000 else print(section)