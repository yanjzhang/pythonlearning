import sys

n,m=sys.stdin.readline().strip().split(' ')
n,m=int(n),int(m)
L=[]
for i in xrange(0,n):
        L.append(sys.stdin.readline().strip().split(' '))
a=[]
b=[]
c=[]
add='add'
list='list'
mod='mod'
de='del'
grep='grep'
for i in xrange(0,n):
        if L[i][0]==add:
                a.append(L[i][1])
                       
        if L[i][0]==list:
                if len(a)>0:
                    for j  in xrange (0,len(a)):
                            print j+1,' ',a[j]
                    print '\n'
                            
        if L[i][0]==mod:
                L[i][1]=int(L[i][1])
                k=L[i][1]
                if k<=len(a):
                        a[k-1]=L[i][2]
               
        if L[i][0]==de:
                L[i][1]=int(L[i][1])
                k=L[i][1]
                if k<=len(a):
                        del  a[k-1]
               
        if L[i][0]==grep:
                k=L[i][1]
                for j in xrange(0,len(a)):
                        if k in a[j]:
                                b.append(a[j])
                                c.append(j)
                for y in xrange(0,len(b)):
                        print c[y]+1,' ',b[y]
                       

