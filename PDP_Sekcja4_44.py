# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 11:44:51 2025

@author: VIK
"""

helloMessage = '"Hello %s!"'

print(helloMessage % ("Kris"))
print(helloMessage % ("Kate"))

helloMessage2 = "%s has %d %s"

print(helloMessage2 % ("Kate",1,"animal"))
print(helloMessage2 % ("Chris",100000,"$"))


helloMessage3 = "{0:s} has {1:d} {2:s}"
 
print(helloMessage3.format("Kate",1,"animal"))
print(helloMessage3.format("Chris",100000,"$"))

line = "{0:20s} costs {1:6d} €"
 
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))

line = '{0:s} {1:d}'
 
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))
