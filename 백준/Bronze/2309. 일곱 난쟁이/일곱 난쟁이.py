import sys;input=sys.stdin.readline
from itertools import combinations as comb

people = sorted(int(input()) for _ in range(9))
select_two = comb(people, 2)

todo_reject = []
for item in select_two: #O(N**2),
    if sum(people) - sum(item) == 100:
        for tmp in item : # O(N), N=2
            todo_reject.append(tmp)
    
    # 2명의 난쟁이를 찾은 경우 BREAK
    if len(todo_reject) >= 2:
        break

for item in people:
    if item not in todo_reject:
        print(item)