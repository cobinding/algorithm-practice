import sys;input=sys.stdin.readline

# t: 테스트 수, n: 해빈의 의상 개수
t=int(input())

for _ in range(t):
    n=int(input().strip())
    days=1

    dic=dict()
    for _ in range(n):
        wear_name, wear_type = input().split()
        
        if dic.get(wear_type):
            dic[wear_type] += 1
        else:
            dic[wear_type] = 1
    
    # 한 종류당 옷이 몇 벌 있는지에 대한 경우의 수
    # 입는5다/입지 않는다 2가지 case 
    for key in dic.keys():
        days *= (dic[key]+1) 

    print(days-1)