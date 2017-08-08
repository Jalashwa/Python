# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:08:10 2016

@author: sagnik
"""

class Rectangle:
    def __init__(self,len,bre):
        self.l=len
        self.b=bre
      
        print len
        print bre
    def Area(self):
        return self.l*self.b
        
rect1=Rectangle(12,12)
print rect1.Area()