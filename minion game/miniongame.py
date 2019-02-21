
def minion_game(string):
    length=len(string)
    v=[]
    c=[]
    for i in string:
        if(i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
            v.append(string.index(i))
        else:
            c.append(string.index(i))

    vscore=0
    cscore=0
    for i in v:
        for j in v[i+1:]:
            vscore+=j-i 
    vscore+=len(v)
    vscore+=v[0]-0
    vscore+=length-v[-1]

    for i in c:
        for j in c[i+1:]:
            cscore+=j-i 
    cscore+=len(c)
    cscore+=c[0]-0
    cscore+=length-c[-1]

    if(vscore>cscore):
        print("Kevin",vscore)
    elif (vscore<cscore):
        print("Stuart",cscore)
    else:
        print("Draw")
            


if __name__ == '__main__':
    s = input()
    minion_game(s)
