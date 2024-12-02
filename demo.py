n,a,b = map(int,input().split())
print(len([i for i in range(1,n+1) if i > a and abs(i-n) <= b]))
