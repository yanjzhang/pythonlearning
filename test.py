#!/usr/bin/python
import sys

def f(x):
        n,m = x.readline().strip().split(' ')
        n,m = int(n),int(m)

        L = []
        for i in xrange(0,n):
                L.append(x.readline().strip().split(' '))
                for j in xrange(0,m):
                        L[i][j] = int(L[i][j])
        return L 

a = f(sys.stdin)
b = f(sys.stdin)

print a,b

#if len(a[0]) == len(b):
#       for i in xrange(0,len(a)):
 #               for k in  xrange(0,len(b[0])):
  #                      sum = 0
   #                     for j in xrange(0,len([a[0]])):
    #                            sum += a[i][j]*b[j][k]
     #                   print sum,
      #          print '\n',

if len(a[0])== len(b):
        for i in range(0,len(a)):
            for y in range(0,len(b[0])):
                sum = 0
                for j in range(0,len(a[0])):
                    sum += a[i][j]*b[j][y]
                print sum,    
            print'\n',

