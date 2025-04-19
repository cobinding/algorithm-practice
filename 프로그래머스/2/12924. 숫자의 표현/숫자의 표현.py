def solution(n):
    
    # num: 계산 시작 값
    # cnt: 연속된 자연수로 n을 표현하는 방법의 수
    # total: 시작값부터 n까지의 연속된 자연수의 합
    num = 1
    cnt = 1
    while True:
        if num == n :
            break
        total = 0
        for i in range(num, n):
            total += i
            if total == n:
                cnt += 1
                total = 0
                break
            if total > n :
                break
        num += 1
        
    return cnt