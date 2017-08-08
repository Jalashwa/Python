# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:35:08 2016

@author: sagnik
"""
class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
   
         
    def Area(self):
        return self.l*self.b
 
len1=input('Enter the length: ')
bre1=input('Enter the breadth: ')
 
len2=input('Enter the length: ')
bre2=input('Enter the breadth: ')  
rect1=Rectangle(len1,bre1)
rect2=Rectangle(len2,bre2)
print rect1.Area()
print rect2.Area()