def sec(h,m,s):
	return 3600*h+60*m+s

def hms(sec):
	return f"{sec//3600} {(sec//60)%60} {sec%60}"

for i in range(3):
	h,m,s,H,M,S=map(int,input().split())
	print(hms(sec(H,M,S)-sec(h,m,s)))
