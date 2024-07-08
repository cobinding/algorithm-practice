import sys;input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))

# k까지의 합(현재의 부분합)
current_sum=sum(arr[:k])
max_sum=current_sum

for i in range(k, n):
    # 가장 왼쪽의 원소를 빼고, 가장 오른쪽의 원소를 더하여 윈도우 슬라이딩
    current_sum=current_sum-arr[i-k]+arr[i]
    max_sum=max(max_sum, current_sum)
     
print(max_sum)