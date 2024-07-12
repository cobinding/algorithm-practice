import sys; input=sys.stdin.readline

# 곱셈과 number 정의
a=int(input())
b=int(input())
c=int(input())
number=str(a*b*c)

num_dic={'0':0, '1':0, '2':0, '3':0, '4':0,
         '5':0, '6':0, '7':0, '8':0, '9':0}

for item in number:
    num_dic[item]+=1
    
for value in num_dic.values():
    print(value)