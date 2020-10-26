# Question Link: https://www.hackerrank.com/challenges/py-set-add/problem

n=int(input())
s= set('')
for i in range (0,n):
    st=input();
    s.add(st);
count =0

for _ in s:
    count+=1
print(count)
