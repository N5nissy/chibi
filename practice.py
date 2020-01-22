data = {}
for i in range(int(input())):
	p,n = input().split();
	data[p] = data.get(p,0) + int(n)
for i, j in sorted([[len(a),a] for a in data.keys()]):
    print (j, data[j])