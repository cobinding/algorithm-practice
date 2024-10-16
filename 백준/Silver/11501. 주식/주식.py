import sys; input=sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]
    total = 0
    for i in range(n-2, -1, -1):
        if max_price > price[i]:
            total += (max_price - price[i])
        else:
            max_price = price[i]

    print(total)