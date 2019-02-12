#!/usr/bin/env python3

testcase=int(input())
for z in range(testcase):
	n=int(input())

	d={}
	count=0

	for i in range(n):
		d["a"+str(i)]=[0]*26
		string=input()
		length=len(string)
		for j in range(length):
			d["a"+str(i)][ord(string[j])-97]+=1

	for i in range(26):
		flag=0
		for j in range(n):
			if(d["a"+str(j)][i]==0):
				flag=1
				break
		if(flag==0):
			count+=1

	print(count)
