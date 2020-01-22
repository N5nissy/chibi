import math
def main():
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    hoge = math.ceil(A / C)
    fuga = math.ceil(B / D)

    if hoge >= fuga:
        print(L - hoge)
    else:
        print(L - fuga)


if __name__ == "__main__":
    main()