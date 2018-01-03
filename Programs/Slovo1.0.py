# -*- coding: cp1251 -*-
#-------------------------------------------------------------------------------
# Name:        Самое длинное слово
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
s = input("Введи строку: ")
a = s.split(" ")
max = 0
c = 0
for i in s.split(" "):
    s1 = len(i)
    if s1>max:
        max = s1
print("Самое(ые) длинное(ые) слово(а) в строке: ")
for i in s.split(" "):
    if len(i) == max:
        print(i)
input()