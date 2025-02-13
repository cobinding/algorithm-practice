def solution(arr, divisor):
    sorted_arr = sorted(arr)
    
    # divisor로 나누어 떨어지는 값 저장
    res = []
    for item in sorted_arr:
        if item%divisor == 0:
            res.append(item)
    
    # 리턴 리스트에 조건별 결과값 생성
    answer = []
    if len(res) == 0:
        answer.append(-1)
    else:
        answer = res
    return answer