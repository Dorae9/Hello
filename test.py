import math
from time import sleep



i11=0
i12=0
i21=0
i22=0

class Point():
    def __init__ (self, input1, input2):
        self.x = input1
        self.y = input2
hemjuur=input("Measurement type: ")

x1= input("x1: ")
if len(x1)==0:
 while i11==0:
  if len(x1)==0:
    print("Please write your number")
    x1=input("x1: ")
    if len(x1)==1:
       i11=1

else :
 y1= input("y1: ")
  
if len(y1)==0:
 while i12==0:
  if len(y1)==0:
    print("Please write your number")
    y1= input("y1: ")
  if len(y1)==1:
     i12=1

else :
 x2= input("x2: ")

if len(x2)==0:
 while i21==0:
  if len(x2)==0:
    print("Please write your number")
    x2= input("x2: ")
  if len(x2)==1:
        i21=1

else :
 y2= input("y2: ")

if len(y2)==0:
 while i22==0:
  if len(y2)==0:
    print("Please write your number")
    y2= input("y2: ")
  if len(y2)==1:
        i22=1

p1=Point(x1,y1)
p2=Point(x2,y2)
lx = abs(float(p1.x)-float(p2.x))
ly = abs(float(p1.y)-float(p2.y))

l = (lx*lx)+(ly*ly)
lr= str(math.sqrt(l))
print("Can't even calculate it by yourself?")

sleep(5)

print("Just joking.")
print("The length between two points is: " + lr + hemjuur)
