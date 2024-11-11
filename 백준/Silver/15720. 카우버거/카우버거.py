import sys;input=sys.stdin.readline

# SET : 버거 1, 사이드 1, 음료 1 각각 10% 할인
b_num, s_num, c_num = map(int, input().split())
cal_sale_num = min(b_num, s_num, c_num)

# 할인이 가능할 때까지 가격 적용
def get_sale_price(price):
    for i in range(cal_sale_num):
        price[i] = price[i] * 0.9
    res = sum(price)
    return res

burgers = sorted(map(int, input().split()), reverse=True)
sides = sorted(map(int, input().split()), reverse=True)
coke = sorted(map(int, input().split()), reverse=True)

# 원래 가격과 세일 가격 계산
total, sale_total = 0, 0
total += (sum(burgers) + sum(sides) + sum(coke))
sale_total += (get_sale_price(burgers) + get_sale_price(sides) + get_sale_price(coke))

print(total)
print(int(sale_total))