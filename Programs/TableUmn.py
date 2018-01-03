# -*- coding: cp1251 -*-
#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      admin
#
# Created:     22.11.2013
# Copyright:   (c) admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
x = int(input("Kakoe chislo umnozhat'? "))
a = int(input("Ot kakogo chisla umnozhat'? "))
b = int(input("Do kakogo chisla umnozhat'? "))
n = int(input("Vvedi shag "))
for i in range(a, b+1, n):
    print(x,"*",i,"=",x*i)
input()