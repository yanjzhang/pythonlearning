import sys

def f():
       x = sys.stdin.readline().strip().split(' ')
        
n,m = f(x)
n,m = int(n),int(m)

a=[]
for i in range(0,n):
        a.append(sys.stdin.readline().strip().split(' '))
        print a[i]

for i in range(0,n):
        for j in range(0,m):
                a[i][j]=int(a[i][j])
print a

p,q = sys.stdin.readline().strip().split(' ')
p,q = int(p),int(q)

b=[]
for x in range(0,p):
        b.append(sys.stdin.readline().strip().split(' '))
        print b[x]

for x in range(0,p):
        for y in range(q):
                b[x][y]=int(b[x][y])
print b

d=[]
if m == p:
    for i in range(0,n):
            c=[]
            for y in range(0,q):
                    sum=0
                    for j in range(0,m):
                            x = j       
                            sum += a[i][j]*b[x][y]
                    c.append(sum)
            d.append(c)

    for i in range(0,n):
            for j in range(0,q):
                    print d[i][j],
            print '\r'

else:
    print 'No'

	
	
	
