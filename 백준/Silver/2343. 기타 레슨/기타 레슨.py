import sys
input=sys.stdin.readline

n,m = map(int, input().split())
lecture = list(map(int, input().split()))

# 시작 값은 가능한 블루레이 크기 중에 가장 작은 값
s, e = max(lecture), sum(lecture)

# 이분탐색을 통해서 가능한 최소 블루레이 크기 정하기
while s<=e:
    mid = (s+e)//2
    
    cnt = 1
    total = 0
    for time in lecture:
        # 시간을 더하다가 mid보다 거치는 순간에 cnt +=1
        # for 문 종료 전에 다시 계산할 수도 있으므로, total = 0으로 최화
        if total + time > mid :
            cnt += 1
            total = 0
        total += time

    # 블루레이 개수가 m보다 작거나 같으면, mid값 갱신
    # 블루레이 개수가 딱 m으로 정해지더라도, 더 최솟값이 있을 수 있으므로 end를 mid - 1로 조정
    if cnt <= m:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
    
print(ans)