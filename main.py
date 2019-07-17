import ctypes as C

lib = C.CDLL("./src/libmymath.so")

lib.add_float.restype = C.c_float
lib.add_float.argtypes = [C.c_float, C.c_float]

print("add_float(2,3):", lib.add_float(2,3))

lib.add_int.restype = C.c_int
lib.add_int.argtypes = [C.c_int,C.c_int]

print("add_int(3,6):", lib.add_int(3,6))

a = C.c_int(3)
b = C.c_int(4)
c = C.c_int()

lib.add_int_ref(C.byref(a), C.byref(b), C.byref(c))
print("add_int_ref(a,b):",c)

a = C.c_float(3)
b = C.c_float(4)
c = C.c_float()

lib.add_float_ref(C.byref(a), C.byref(b), C.byref(c))
print("add_float_ref(a,b):",c)

a = (C.c_int * 3) (3,4,5)
b = (C.c_int * 3) (5,4,3)
c = (C.c_int * 3) (0,0,0)
lib.add_int_array(C.byref(a), C.byref(b), C.byref(c), C.c_int(3))
print(c2[1])
