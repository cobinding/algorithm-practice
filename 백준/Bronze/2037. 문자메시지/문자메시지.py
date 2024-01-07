import sys; input=sys.stdin.readline

p, w = map(int, input().rstrip().split())
word = input().rstrip()
dic = {1: [' '], 2: ['A','B','C'], 3:['D','E','F'], 4:['G','H','I'], 
       5: ['J','K','L'], 6:['M','N','O'], 7:['P','Q','R','S'],
       8: ['T','U','V'], 9:['W','X','Y','Z']}
score = 0
key_score = []

# 숫자 누르는 횟수
for spel in word:
    for k, v in dic.items():
        for item in v :
          if item == spel : 
                score += p*(v.index(item)+1)
                key_score.append(k)

flag = False
cnt = 0     
# 연속된 숫자가 나오는 횟수 
for i in range(1, len(key_score)) :
    if key_score[i-1] == key_score[i]:
        
        if key_score[i] != 1:
            flag = True
            cnt += 1
    else:
        flag = False
        
print(score + cnt*w)