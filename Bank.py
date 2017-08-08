# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:28:36 2016

@author: sagnik
"""

class Bank:
    def __init__(self,a,b):
        self.accNum=a
        self.balance=b
    
    def Credit(self,addMon):
        self.balance += addMon
        
    def Debit(self,outMon):
        if outMon <= self.balance:
            self.balance -= outMon
        else:
            print('Not sufficient balance in the account')
            print('Transaction cancelled')

    def getData(self):
        print self.accNum
        print self.balance
        
Person1=Bank(11234,1000)
print Person1.getData()

Person1.Credit(200)
print Person1.getData()        
            
Person1.Debit(990)
Person1.getData()        