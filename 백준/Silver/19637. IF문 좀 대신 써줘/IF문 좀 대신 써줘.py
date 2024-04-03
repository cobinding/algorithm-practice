import sys; input=sys.stdin.readline

n,m=map(int,input().split())
name_arr=[]
val_arr=[]

# 칭호 정보 저장 | name_arr, val_arr은 같은 인덱스로 값을 찾을 수 있다.
for _ in range(n):
    name,value=input().split()
    name_arr.append(name)
    val_arr.append(int(value))

for _ in range(m):
    target=int(input())
    ans=0

    left, right = 0, len(name_arr)-1
    while left <= right:
        mid = (left+right)//2
        
        if target <= val_arr[mid]:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    
    print(name_arr[ans])