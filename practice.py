num = int(input())
L = [int(x) for x in input().split()]
L.append(2020)
input()
s = [int(x)-1 for x in input().split()]

for i in s:
    if L[i+1] > L[i] +1:
        L[i] += 1

for i in range(len(L) -1):
    print(L[i])