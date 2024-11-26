n = int(input())
sing = ['baby', 'sukhwan', 'tururu', 'turu',
       'very', 'cute', 'tururu', 'turu',
       'in', 'bed', 'tururu', 'turu',
       'baby', 'sukhwan']

# 노래의 단어가 몇 번째 sing에 속하는지 연산
idx = n % len(sing) - 1
k = n // len(sing)

# tururu, turu의 idx
tururu = [2, 3, 6, 7, 10, 11]

if idx in tururu:
    # 노래 반복 횟수(k)만큼 'ru' 추가
    tmp = sing[idx] + "ru" * k
    ruNum = tmp.count("ru")
    # "ru"가 5번 이상 나오면, 조건에 맞게 출력
    if ruNum >= 5:
        print("tu+ru*%d" % ruNum)
    else:
        print(tmp)

else:
    print(sing[idx])
