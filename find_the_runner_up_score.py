if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    array = set(arr)
    array = sorted(array)
    
    print(array[-2])
    