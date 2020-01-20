x1 = input("あなたの生年月日を入力してください: ")
def digitSum(x):
    if len(x) is 1:
        return x
    array = list(map(int, list(x)))
    return digitSum(str(sum(array)))   
if __name__ == "__main__":
    n = x1
    x = str(n)
    result1 = digitSum(x)
   
x2 = input("相手の生年月日を入力してください: ")
def digitSum(x):
    if len(x) is 1:
        return x
    array = list(map(int, list(x)))
    return digitSum(str(sum(array)))   
if __name__ == "__main__":
    n = x2
    x = (n)
    result2 = digitSum(x)
   
if  result1==result2:
    print ('抜群')
elif abs(int(result1)-int(result2)) <3:
    print ('最高')
elif abs(int(result1)-int(result2)) <7:
    print ('普通')
else:
    print ('残念')


