import sys; input = sys.stdin.readline

price = int(input().rstrip())
change = 1000 - price

coin = [500, 100, 50, 10, 5, 1]
cnt = 0

for item in coin:
    cnt += (change // item)
    change %= item

print(cnt)