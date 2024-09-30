from sys import stdin
input = stdin.readline


def match(x,y):
    for cx,cy,typ in tmp:
        # 현재 값이 정해지면 return
        if cx==x and cy==y: return False
        
        if typ == 1: 
            if x<cx and y==cy:
                continue
            return False
        elif typ == 2:
            if x<cx and y>cy:
                continue
            return False
        elif typ == 3:
            if x==cx and y>cy:
                continue
            return False
        elif typ == 4:
            if x>cx and y>cy:
                continue
            return False
        elif typ == 5:
            if x>cx and y==cy:
                continue
            return False
        elif typ == 6:
            if x>cx and y<cy:
                continue
            return False
        elif typ == 7:
            if x==cx and y<cy:
                continue
            return False
        elif typ == 8:
            if x<cx and y<cy:
                continue
            return False
    return True


n,m = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(m)]

# 일단 (1,1)부터 비교하면서 탐색
for i in range(1, n+1):
    for j in range(1, n+1):
        if match(i,j): 
            print(i,j)