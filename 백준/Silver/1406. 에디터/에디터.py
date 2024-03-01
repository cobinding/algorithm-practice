import sys;input=sys.stdin.readline
from collections import deque

s=input().rstrip()
stack1, stack2=list(s), []
n=int(input())

for _ in range(n):
    word=input().rstrip()
    if word=="L" and len(stack1) != 0 :
        stack2.append(stack1.pop())
    elif word=="D" and len(stack2) != 0 :
        stack1.append(stack2.pop()) 
    elif word=="B" and len(stack1) != 0 :
        stack1.pop()
    elif word[0]=="P":
        p,x=word.split()
        stack1.append(x)

print(''.join(stack1 + list(reversed(stack2))))
