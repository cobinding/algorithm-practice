import sys; input=sys.stdin.readline

n=int(input().rstrip())
dic = dict()

for _ in range(2*n-1):
    name = input().rstrip()
    if dic.get(name):
        dic[name] += 1
    else:
        dic[name] = 1
    
for k,v in dic.items():
    if v % 2 == 1 : 
        print(k)