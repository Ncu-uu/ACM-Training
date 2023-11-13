while 1:
    try:
        sum=0
        n=int(input())
        while n:
            op=n%10
            if op%2==0:
                sum+=op
            n//=10
        print(sum)
        sum=0
    except:
        break
        