import copy
def bubble(box,n):
    for i in range(n):
        p=n-1
        while p!=i:
            if box[p][1]<box[p-1][1]:
                box[p],box[p-1]=box[p-1],box[p]
            p -=1
    return box

def selection(box,n):
    for i in range(n):
        mini=i
        for j in range(i,n):
            if box[j][1]<box[mini][1]:
                mini=j
        if box[i][1]>box[mini][1]:
            box[i],box[mini]=box[mini],box[i]
    return box

n=int(input())
A=list(input().split())
B=copy.deepcopy(A)

bubble=bubble(A,n)
print(*A)
print("Stable")
selection=selection(B,n)
print(*B)
print("Stable" if A==B else "Not stable")