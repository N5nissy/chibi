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
    print(int(result1))
