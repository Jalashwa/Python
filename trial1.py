# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 00:13:50 2016

@author: sagnik
"""

def Block1():
    global x
    x='AAA'
    print x

def Block2():
    global y,z
    y='AAA'
    z=' A '
    print y
    print z

def Block3():
    global a,b,c
    a='A'
    b='A'
    c='A'     
    print a
    print b
    print c

print x,
print y,
print a
print ('   '),
print z,
print b
print ('       '),
print c

feed=input("Enter the Block Number to move:")

list=[1,2,3,4] 
if feed==1:
    for num in list:
        print('\n')
    print x
else:
    print("The number is rejected")   
    

  