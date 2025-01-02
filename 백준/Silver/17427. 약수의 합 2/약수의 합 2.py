import sys;input=sys.stdin.readline

n = int(input())

# 약수는 배수인 성질
num = 0
for i in range(1, n+1): # O(N)
    # 단순 계산 복잡도는 O(1)
    num += (n//i) * i

print(num)