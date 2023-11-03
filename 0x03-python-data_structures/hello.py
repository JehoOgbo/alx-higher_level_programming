import ctypes

lib = ctypes.CDLL("./hello.so")  # get the cdll of the .so into a data type

l = ['hello', 'world', 'this is good']

lib.hello()
# not same name of function and then .argtypes
lib.print_list.argtypes = [ctypes.py_object]  # must specify type of argument
# Must use py_object for PyObject as it is what is defined in ctypes module
lib.print_list(l)
# This gives ability to use a list from a python script inside a c function

del l[1];


lib.print_list(l)

num = 78
l.append(num)
l.append(56)

lib.print_list(l)
