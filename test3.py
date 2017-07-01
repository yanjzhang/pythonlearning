import sys

def f(x):
        n,m = x.readline().strip().split('')
        return n,m

def add(x):
        a=[]
        a.append(x)
        return a

def del(x):
        if x in xrange(0,len(a)):
                a[x-1]=[]

def mod(x,y):
        if x in xrange(0,len(a)):
                a[x-1]=y

def list():
        for i in xrange(0,len(a)):
                k=i+1
                print k +' '+a[i]

def grep(x):
        b=[]
        y=0
        for i in xrange(0,len(a)):
                if x in a[i]:
                        y=y+1
                        b.append(a[i])
        for i in xrange(0,y):
                i+=1
                print i+b[i] 

a=f(sys.stdin)
c=[]
if a[0] == add:
       b= add(a[1])
       print b
