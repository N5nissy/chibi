n = int(input())
k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    if min(a, b, n-a+1, n-b+1)%3 == 0:
        print(3)
    elif min(a, b, n-a+1, n-b+1)%3 == 1:
        print(1)
    else:
        print(2)