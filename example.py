Scores = [int(input()) for i in range(5)]
for j in range(len(Scores)):
    if Scores[j] < 40:
        Scores[j] = 40
print(sum(Scores)//5)