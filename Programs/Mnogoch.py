# -*- coding: cp1251 -*-
#-------------------------------------------------------------------------------
# Name:        Многочлен
# Purpose:
#
# Author:      admin
#
# Created:     21.11.2013
# Copyright:   (c) admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import math
a = int(input("write a "))
b = int(input("write b "))
c = int(input("wrice c "))
if (b>0):                                           #Настройка вывода уравнения на экран
    if (c>0):
        print("We have", a,"x^2 +",b,"x +",c,"= 0")
    elif (c<0):
        print("We have", a,"x^2 +",b,"x",c,"= 0")
elif (b<0) and (c<0):
    print("We have",a,"x^2",b,"x",c,"= 0")
else:
    print("We have",a,"x^2",b,"x +",c)
x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)               #Корень 1
x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)               #Корень 2
print("x1=",x1,"x2=",x2)
input()