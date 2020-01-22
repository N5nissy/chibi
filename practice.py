if __name__ == '__main__':

	input()
	A = set(map(int,input().split()))
	int(input())
	B = set(map(int,input().split()))

	if B <= A:
		print("1")
	else:
		print("0")
