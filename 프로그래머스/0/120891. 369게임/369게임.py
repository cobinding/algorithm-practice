def solution(order):
    s = str(order)
    cnt = 0
    for item in s:
        if item == '3' or item == '6' or item =='9':
            cnt += 1
    return cnt