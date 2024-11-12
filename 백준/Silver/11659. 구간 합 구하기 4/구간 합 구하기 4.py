from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().split()))

psum = [0]*(n+1)
for i in range(1,n+1) :
     psum[i] = psum[i-1] + li[i-1]

for i in range(m) :
     i,j = map(int, input().split())
     print(psum[j]-psum[i-1])