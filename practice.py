n, k = map(int, input().split())
ans = []
for i in range(2**n):
    cnt = 0
    for j in range(n):
        if i>>j&1 ==1:
            cnt += 1
    if cnt == k:
        st = []
        for t in range(n):
            if i>>t&1 ==1:
                st.append(t)
        print("{}:".format(i),end =" ")
        print(*st)
