a,b,c,students=map(int,input().split())

# a*i + b*j + c*k = students
ans = 0
for i in range(students//a+1):
    for j in range(students//b+1):
        for k in range(students//c+1):
            if students == (a*i + b*j + c*k):
                print(1)
                exit()

print(0)