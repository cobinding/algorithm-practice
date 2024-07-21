import sys; input=sys.stdin.readline

n = int(input())
arr = sorted(map(int,input().split()))
like = 0

for i in range(n):
    
    # 배열의 숫자마다 다 검사를 해야하므로 i가 + 될 때마다 그를 위한 포인터 지정
    left, right = 0, n-1
    
    # 처음 시작할 때 겹치는 부분 제거 
    if i == 0 : left += 1
    if i == n-1 : right -= 1
  
    # 서로 다른 두 수이기 때문에 <=가 아닌 <로 조건
    while left < right:
        total = arr[left] + arr[right]
        if total == arr[i]:
            like += 1
            break
        elif total < arr[i]:
            left += 1
            # 배열에서 비교를 위해 선택된 수가 포인터와 겹친다면 한번 더 증가함으로써 겹치지 않게 해줌
            if i == left : left += 1
        elif total > arr[i]:
            right -=1
            if i == right : right -= 1

print(like)