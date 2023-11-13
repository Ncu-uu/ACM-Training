a=[0]*1001
oc=0
ic=(int)(input())
for i in range(0,ic+1):
    n=(eval)(input())
    k=(eval)(input())
    a[n]+=k

ic=input()
for i in range(0,ic+1):
    n=(eval)(input())
    k=(eval)(input())
    a[n]+=k    

for i in range(1,1002):
    if (a[i]!=0):
        oc+=1

print(oc)

for i in range(1000,-1,-1):
    if (a[i]!=0):
        print(" {} {:.1f}".format(i,a[i]))
    
    