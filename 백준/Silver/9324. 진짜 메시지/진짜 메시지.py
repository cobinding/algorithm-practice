t = int(input())
for _ in range(t):
    word = input()

    # word의 스펠링과 각 인덱스를 저장할 Hash
    d = dict()
    for i in range(len(word)):
        # 이미 Key로 선정되었다면, 인덱스 저장
        key = word[i]
        if not d.get(key):
            d[key] = [i]
        else:
            d[key].append(i)

    wordIdx = list(d.values())
    printFlag = True

    for arr in wordIdx :
        idxCnt = len(arr)
        flag = True

        # 딱 3만큼 등장한다면 FAKE
        if idxCnt == 3:
            flag = False

        elif idxCnt > 3:
            # 7개 이상 반복되는 경우 4개씩 등장하지 않으면 FAKE
            if idxCnt % 4 == 3:
                flag = False
            # 바로 뒤에 추가가 되었는지 확인
            for i in range(3, idxCnt, 4):
                if arr[i] - arr[i-1] != 1:
                    flag = False

        if not flag:
            printFlag = False
            break

    print("OK" if printFlag else "FAKE")