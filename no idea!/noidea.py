#!/usr/bin/env python3

n,m = [int(x) for x in input().split(" ")]
a=[0]*1000000

t=[int(k) for k in input().split(" ")]
for i in range(n):
    a[t[i]]+=1

pos=0
neg=0

u=[int(k) for k in input().split(" ")]
for i in range(m):
    pos+=a[u[i]]

v=[int(k) for k in input().split(" ")]
for i in range(m):
    neg+=a[v[i]]

ans=pos-neg
print(ans)

