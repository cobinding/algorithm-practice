a,b,c,students=map(int,input().split())

# a*i + b*j + c*k = students
ans = 0
for i in range(students//a):
    for j in range(students//b):
        for k in range(students//c):
            if students == (a*i + b*j + c*k):
                print(1)
                exit()

print(0)