import sys
input=sys.stdin.readline

n=int(input())
lo, hi = 0, n

while lo <= hi:
    mid = (lo + hi) // 2
    
    if mid**2 < n:
        lo = mid + 1
    elif mid**2 >= n:
        hi = mid - 1
    
print(lo)