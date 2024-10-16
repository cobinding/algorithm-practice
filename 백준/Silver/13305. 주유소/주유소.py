import sys; input=sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

curr_price = price[0]
total = curr_price * km[0]

for i in range(1, n-1):
    if price[i] < curr_price:
        curr_price = price[i]
    total += curr_price * km[i]

print(total)