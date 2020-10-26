# Link to the question : https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input());
noOfShoes = map(int,input().split());
#print(noOfShoes);
dic= Counter(noOfShoes);
earning =0
customers= int(input());
for i in range (0,customers):
    shoeSize,cost = map(int,input().split());
    if dic[shoeSize]>0 :
        earning+=cost
        dic[shoeSize]-=1
print(earning)

