import sys;input=sys.stdin.readline

ans=[]
while True:
    s=input().rstrip()
    stack=[]
    cnt=0
    
    if '-' in s : break
    
    for i in range(len(s)) :
        # { 라면
        if s[i] == '{' : 
            stack.append('{')
        
        # 스택이 비어있고, } 라면 안정적이지 않으므로 counting
        elif len(stack) == 0 and s[i] == '}':
            stack.append('}')
            cnt += 1
        
        # 스택이 비어있지 않고, } 라면 안정적일 가능성있으므로 stack.pop
        elif len(stack) != 0 and s[i] == '}':
            stack.pop()
         
    cnt += len(stack)//2
    ans.append(cnt)
    
for i in range(len(ans)):
    print(str(i+1)+'.', ans[i])