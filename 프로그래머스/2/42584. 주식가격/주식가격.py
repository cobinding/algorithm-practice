def solution(prices):
    # 몇초 후 가격이 떨어지는지 저장
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # prices의 인덱스
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack:
            top = stack[-1]
            
            # 주식 가격이 떨어졌다면
            # 현재 인덱스 시점에서 stack의 top까지 얼마나 떨어졌는지 차이 저장
            if prices[top] > prices[i]:
                answer[top] = i - top
                stack.pop()
            
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break
        
        # 스택 추가
        # 다음 시점으로 넘어갔을 때 다시 비교 대상
        stack.append(i)
    
    return answer