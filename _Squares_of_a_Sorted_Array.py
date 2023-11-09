n=int(input())
s=list(map(int,input().split()))
l=list(set(s))
l.sort()
for i in range(len(l)):
    l[i]=l[i]*l[i]
l.sort()
print(*l)