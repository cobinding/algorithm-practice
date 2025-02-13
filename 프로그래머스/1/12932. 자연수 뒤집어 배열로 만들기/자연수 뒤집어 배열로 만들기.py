def solution(n):
    # 문자열로 변경
    s = str(n)
    
    # 문자열 s를 역순으로 res 리스트에 저장
    res = []
    for i in range(len(s)-1, -1, -1):
        res.append(int(s[i]))
    
    return res