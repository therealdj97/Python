# #atan2
# from cmath import pi
# from math import atan2
# def calcAngleDegrees(x,y): 
#     return atan2(y,x)/pi

# calcAngleDegrees()

from cmath import pi
import math
x=int(input("enter x axis value"))
y=int(input("enter y  axis value"))

print(math.atan2(x,y)*180/pi)