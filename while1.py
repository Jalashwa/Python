# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:51:05 2016

@author: sagnik
"""
import sys

while 1: 
    name = raw_input("Name: ")
    if name == "":
        print "Oops! Retry"
        sys.exit()
    else:
        print "Hello", name
        sys.exit()  