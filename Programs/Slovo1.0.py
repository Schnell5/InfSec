# -*- coding: cp1251 -*-
#-------------------------------------------------------------------------------
# Name:        ����� ������� �����
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
s = input("����� ������: ")
a = s.split(" ")
max = 0
c = 0
for i in s.split(" "):
    s1 = len(i)
    if s1>max:
        max = s1
print("�����(��) �������(��) �����(�) � ������: ")
for i in s.split(" "):
    if len(i) == max:
        print(i)
input()