#!/usr/bin/env python3

testcase=int(input("enter no of test case:"))
for z in range(testcase):
	n=int(input("enter no of strings you will enter to count common characters in them:"))

	d={}
	count=0

	for i in range(n):
		d["a"+str(i)]=[0]*26
		string=input("enter string {} : ".format(i+1))
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

	print("no of common char in above all strings are :",count)
