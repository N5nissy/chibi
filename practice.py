import itertools

if __name__ == '__main__':

	n = int(input())
	seq = list(itertools.permutations(range(1,n+1)))

	for p in seq:
		print(*p)
