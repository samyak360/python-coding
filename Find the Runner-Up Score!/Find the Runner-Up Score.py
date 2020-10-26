if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    #print(arr);
    arr=set(arr);
    #print(arr);
    arr=list(arr);
    #print(arr);
    arr.sort(reverse=True);
    print(arr[1]); 
