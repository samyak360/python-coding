testcase=int(input())

for z in range (testcase):
    host=input()
    child=input()

    beg=[]
    num=host.count(child[0])
    beg.append(host.find(child[0]))

    ans=[]
    a=1
    b=0
    c=1

    if child in host:
        print("Yes")
        print(0)
        continue

    else:
        for i in range(num):
            for a in range(beg[i]+1,len(host)):

                if c>=len(child):
                    break

                if host[a]==child[c]:
                    c+=1
                    continue

                if host[a]!=child[c]:
                    b+=1
                    continue

            if len(host)-beg[i]>=len(child) and c>=len(child):
                ans.append(b)

            b=0
            c=1
            beg.append(host.find(child[0],beg[i]+1))
    
    ans.sort()
    if len(ans)==0:
        print("No")
    else:
        print("Yes")
        print(ans[0])
