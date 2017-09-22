'''from ctypes import cdll

msvcrt = cdll.msvcrt
message_string = b'Hello World!\n'
msvcrt.printf(b'Testing: %s', message_string)
'''

from ctypes import c_int, c_long, c_char
from _ctypes import Union
class barley_amount(Union):
    _fields_ = [
        ("barley_long", c_long),
        ("barley_int", c_int),
        ("barley_char", c_char * 8)]

value = input("Enter the amount of barley to put into the beer vat: ")
my_barley = barley_amount(int(value))
print("Barley amount as a long: {name}".format(name = my_barley.barley_long))
print("Barley amount as an int: {name}".format(name = my_barley.barley_int))
print("Barley amount as a char: {name}".format(name = my_barley.barley_char))