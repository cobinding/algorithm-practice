import sys;input=sys.stdin.readline

m=int(input())
arr=[0,1,2,3]
tmp_x=0
flag=False
for _ in range(m):
    x,y=map(int,input().split())

    
    # x 먼저 찾기
    for i in range(len(arr)):
        if arr[i]==x:
            tmp_x=arr[i]
        
            # 이후 y 찾기
            for j in range(len(arr)):
                if arr[j]==y:
                    arr[i]=arr[j]
                    arr[j]=tmp_x
                    flag=True
                    break
            if flag:break
                    
print(arr[1])