import sys;input=sys.stdin.readline

a,b=map(int,input().split())

# 배열 만들기
number=1
arr=[0]
for i in range(1,b+1):
    arr+=[number]*i
    number+=1
    
# 구간 [a,b] 숫자들의 합
sum_numbers=0
for index in range(a,b+1):
    sum_numbers+=int(arr[index])

print(sum_numbers)