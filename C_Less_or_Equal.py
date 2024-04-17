n, k = map(int, input().split())
 
a = list(map(int, input().split()))
 
a.sort()
 
if k == 0 and a[0] > 1:
    print(1)
elif k == 0 and a[0] == 1:
    print(-1)
elif k <= n -1:
    if a[k-1] == a[k]:
        print(-1)
    else:
        print(a[k-1])
elif k == n:
    print(a[-1])
