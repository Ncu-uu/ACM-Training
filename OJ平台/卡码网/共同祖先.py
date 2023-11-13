while 1:
    try:
        n = int(input())
        m=[1]
        y=[2]
        for i in range(n):
            a,b=map(int,input().split())
            if a==m[-1]:
                m.append(b)
                m.sort()
            elif a==y[-1]:
                y.append(b)
                y.sort()
        if len(m)>len(y):
            print("You are my elder")
        elif len(m)==len(y):
            print("You are my brother")
        else:
            print("You are my younger")
    except:
        break
                    