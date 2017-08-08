# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:26:29 2016

@author: sagnik
"""
import sys

len1=raw_input('Enter the length: ')
bre1=raw_input('Enter the breadth: ')

len2=raw_input('Enter the length: ')
bre2=raw_input('Enter the breadth: ')

if len1=="" or len2=="" or bre1=="" or bre2=="":
    print('no Input')
    sys.exit()
else:
    
    class Rectangle:
        def __init__(self,length,breadth):
            self.l=int(length)
            self.b=int(breadth)
   
            
        def Area(self):
            return self.l*self.b

  

rect1=Rectangle(len1,bre1)
rect2=Rectangle(len2,bre2)
print rect1.Area()
print rect2.Area()