def solution(s):
    arr = s.split(" ")
    int_arr = list(map(int, arr))
    
    answer = ""
    min_val, max_val = min(int_arr), max(int_arr)
    answer += str(min_val)
    answer += " "
    answer += str(max_val)
    
    return answer