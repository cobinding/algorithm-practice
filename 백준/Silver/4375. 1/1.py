import sys;input=sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break

    num = 0
    i = 1
    while True:
        # 1%m, 11%m, 111%m ....은 결국 (이전 식 * 10 + 1) % n
        # 예를 들어, 111%n = ((11%n) * 10 + 1) % n
        num = (num * 10 + 1) % n

        # 나누어 떨어져, n의 배수인 경우
        if num == 0 :
            print(i)
            break
        i += 1
