n = int(input())
dic = dict()
least_name = []

for _ in range(n):
    name = input().split()
    key = name[0]
    
    # enter와 leave 카운트
    if dic.get(key): dic[key] += 1
    else: dic[key] = 1

# 1번만 카운트 된 사람 == 아직 남아 있는 사람
for k, v in dic.items():
    if v % 2 == 1 :
        least_name.append(k)
    
ans = sorted(least_name, key = lambda x : x, reverse = True)
for i in ans:
    print(i)