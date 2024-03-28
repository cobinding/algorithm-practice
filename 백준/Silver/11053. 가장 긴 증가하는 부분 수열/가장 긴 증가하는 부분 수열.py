n = int(input())
li = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n) : 
    for j in range(i) : 
        # 0부터 i까지니까 앞의 수들 검사 가능..
        if li[i] > li[j] : 
            # 증가하면 갱신
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))