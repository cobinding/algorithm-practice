def solution(s):
    answer = True
    stack = []
    
    for item in s :
        if item == '(':
            stack.append('(')
        elif item == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                answer = False
                
    if len(stack) != 0:
        answer = False
    return answer