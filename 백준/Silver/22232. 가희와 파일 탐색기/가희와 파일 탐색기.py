import sys;input=sys.stdin.readline

n,m=map(int, input().split())

jo_test = [input().rstrip() for _ in range(n)]
ext = set(input().rstrip() for _ in range(m))

jo_test_split = []
for item in jo_test:
    jo_test_split.append(item.split("."))


# 첫 번째 정렬  
jo_test_split = sorted(jo_test_split, key=lambda x : (x[0], x[1]))

# 두 번째 정렬
for i in range(n-1):
    # 파일명이 같은 경우
    if jo_test_split[i][0] == jo_test_split[i+1][0]:
        # 뒷순서의 파일의 확장자만 존재하는 경우
        if jo_test_split[i][1] not in ext and jo_test_split[i+1][1] in ext:
            tmp = jo_test_split[i]
            jo_test_split[i] = jo_test_split[i+1]
            jo_test_split[i+1] = tmp
           
for item in jo_test_split:
    print(item[0]+"."+item[1])