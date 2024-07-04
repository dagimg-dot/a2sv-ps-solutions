t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_sum = 0
    curr_max = a[0]
    curr_sign = 1 if a[0] > 0 else -1
    
    for i in range(1, n):
        if (a[i] > 0 and curr_sign == -1) or (a[i] < 0 and curr_sign == 1):
            total_sum += curr_max
            curr_max = a[i]
            curr_sign *= -1
        else:
            curr_max = max(curr_max, a[i])
    
    total_sum += curr_max
    print(total_sum)
