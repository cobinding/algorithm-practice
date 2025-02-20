def solution(arr):
    
    ans = []
    
    # 하나씩 돌면서 스택에 넣기
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            ans.append(arr[i])
    ans.append(arr[-1])
    
    return ans