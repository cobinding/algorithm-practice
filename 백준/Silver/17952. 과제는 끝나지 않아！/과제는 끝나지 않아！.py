import sys;input=sys.stdin.readline

t=int(input())

homework = []
total = 0
for _ in range(t):
    n = input()
    
    if n[0] == '0' and len(homework) != 0:
        num = homework.pop()
        num[-1] -= 1
        
        if num[-1] == 0 :
            total += num[1]
        else:
            homework.append(num)
        
    elif n[0] == '1':
        li = list(map(int, n.split()))
        li[-1] -= 1
        
        if li[-1] == 0 :
            total += li[1]
        else:
            homework.append(li)
        print
        
print(total)