# 행: row, 열: col

row = {'8':0, '7':1, '6':2, '5':3, '4':4, '3':5, '2':6, '1':7}
col = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
move = {'R':(0,1), 'L':(0,-1), 'B':(1,0), 'T':(-1,0), 'RT':(-1,1), 'LT':(-1,-1), 'RB':(1,1), 'LB':(1,-1)}


king, rock, n = input().split()
n=int(n)
graph = [[0 for _ in range(8)] for _ in range(8)] # 8*8 체스판


king_row, king_col = row[king[1]], col[king[0]]
rock_row, rock_col = row[rock[1]], col[rock[0]]
graph[rock_row][rock_col] = 1

for _ in range(n):
    command = input()
    r,c = move[command][0], move[command][1]
    
    if (0 <= king_row+r < 8 and 0 <= king_col+c < 8):
        # 돌이랑 같은 곳으로 이동할 때
        if (king_row+r == rock_row) and (king_col+c == rock_col):
            if (0 <= rock_row+r < 8 and 0 <= rock_col+c < 8):
                rock_row += r
                rock_col += c
                king_row += r
                king_col += c
        else:
            king_row += r
            king_col += c
            
            
king_position=str()
for k,v in col.items():
    if v == king_col:
        king_position += k
            
for k,v in row.items():
    if v == king_row:
        king_position += k

print(king_position)

rock_position=str()
for k,v in col.items():
    if v == rock_col:
        rock_position += k
        
for k,v in row.items():
    if v == rock_row:
        rock_position += k
    
print(rock_position)