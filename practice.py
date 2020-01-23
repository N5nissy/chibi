r, c = map(int, input().split())

mat = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
    mat[i] = list(map(int, input().split()))

for i in range(r):
    s = sum(mat[i])
    mat[i].append(s)

for j in range(c):
    s = 0
    for i in range(r):
        s += mat[i][j]
    mat[r][j] = s

mat[r][c] = (sum(mat[r]))

for i in range(r+1):
    for j in range(c+1):
        if j == c:
            print(str(mat[i][j]))
        else:
            print(str(mat[i][j]) + " ", end="")