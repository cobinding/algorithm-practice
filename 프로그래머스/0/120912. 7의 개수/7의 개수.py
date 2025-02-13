def solution(array):
    
    cnt = 0
    for item in array:
        item = list(str(item))
        cnt += item.count('7')
    return cnt