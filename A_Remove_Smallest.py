t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    if len(a) == 1 or a == [a[0]] * len(a):
        print("YES")
        continue

    diff = []
    for i in range(1, len(a)):
        diff.append(abs(a[i] - a[i - 1]))

    for d in diff:
        if d > 1:
            print("NO")
            break
    else:
        print("YES")

