def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97, 123) if not chr(i) in skip]
    s = list(s)
    
    for i in range(len(s)):
        if alphabet.index(s[i]) + index < len(alphabet)-1:
            s[i] = alphabet[alphabet.index(s[i]) +index]
        else:
            s[i] = alphabet[(alphabet.index(s[i])+index)%len(alphabet)]

    answer = ""
    for i in s:
        answer += i
    return answer