import sys;input=sys.stdin.readline

# n: 도감에 수록된 포켓몬 수
# m: 내가 맞춰야 하는 문제의 개수
n,m = map(int, input().split())

d_num = dict()
d_name = dict()

for i in range(1, n+1):
    pocketmon = input().rstrip()

    # d_name - key: name / value: int
    d_name[pocketmon] = i
    # d_num - key: int / value: name
    d_num[i] = pocketmon

# 알파벳 -> 번호
# 번호 -> 알파벳 출력
for _ in range(m):
    item = input().rstrip()

    if item.isdigit() == True : # 숫자로 이루어져 있을 때(str형 숫자도 트래킹 가능) -> d_num 도감 찾아야함
        print(d_num[int(item)])
    else:
        print(d_name[item])