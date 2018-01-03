#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        модуль1
# Purpose:
#
# Author:      admin
#
# Created:     19.03.2014
# Copyright:   (c) admin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    pass

if __name__ == '__main__':
    main()
okl = int(input('Oklad: '))
prc = int(input('% naloga: '))
nalog = okl*prc/100
z_p = okl - nalog
print('Nalog:', nalog, '\n Z/p: ',z_p)
