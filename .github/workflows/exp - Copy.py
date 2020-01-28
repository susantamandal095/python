#!/usr/bin/python
import collections

numbercount = collections.Counter()
with open("C:/python27/Out.txt") as file:
    for line in file:
       numbercount.update(line.split())

for k,v in numbercount.iteritems():
                # print k , v
                 x =int (k)
                 y =int (v)
                 print x,y
                 e = x*y
                 print("the val of e is :",e)
                
            
            
           
             
        
