def main():
    a = []
    b = []
    for _ in range(10):
        a.append(int(input()))
    for _ in range(10):
        b.append(int(input()))
    a.sort(reverse = True)
    b.sort(reverse = True)

    aa = 0
    bb = 0
    for x in range(3):
        aa += a[x]
        bb += b[x]

    print(aa, bb)

if __name__ == "__main__":
    main()