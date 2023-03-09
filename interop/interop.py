import numpy as np
import random

def run(val_int, val_dbl, val_str, val_intarray, val_dblarray, val_dblarray_re, val_dblarray_im, val_bool_2darray, cluster):
    
    print(type(val_int))
    print(val_int)
    print()

    print(type(val_dbl))
    print(val_dbl)
    print()
    
    print(type(val_str))
    print(val_str)
    print()
    
    print(type(val_intarray))
    print(type(val_intarray[0]))
    print(val_intarray)
    print()

    print(type(val_intarray))
    print(type(val_intarray[0]))
    print(val_intarray)
    print()
    
    print(type(val_dblarray))
    print(type(val_dblarray[0]))
    print(val_dblarray)
    print()
    
    # LabVIEWからPythonに直接Complexを渡せないので、real, imageを別々に渡してPythonでcomplexに変換する。
    print(type(val_dblarray_re))
    print(type(val_dblarray_re[0]))
    print(val_dblarray_re)    
    print(type(val_dblarray_im))
    print(type(val_dblarray_im[0]))
    print(val_dblarray_im)
    print()

    # doubleから複素数に変換する
    val_complex_array = np.array(np.vectorize(complex)(val_dblarray_re, val_dblarray_im))    
    print(type(val_complex_array))
    print(type(val_complex_array[0]))
    print(val_complex_array)    
    print()

    print(type(val_bool_2darray))
    print(type(val_bool_2darray[0][0]))
    print(val_bool_2darray)    
    print()    

    # cluster
    print(type(cluster))
    print(cluster)
    print()

    # 入力待ち
    #input()

def return_two_arrays():        
    # return value
    ret_tuple =  [random.random() for i in range(3)], [random.choice([True, False]) for i in range(3)]
    ret1 = ret_tuple
 
    print(type(ret1))
    print(ret1)

    return ret1

def return_tuple_arrays():        
    # return value
    ret_tuple =  [random.random() for i in range(3)], [random.choice([True, False]) for i in range(3)]
    ret1 = [ret_tuple, ret_tuple]
 
    print(type(ret1))
    print(ret1)

    return ret1

# h_re = [i for i in range (16)]
# h_im = np.zeros(16)
# print(h_re, h_im)
# run(h_re, h_im)

# return value
# ret_tuple =  ([0, 1, 2, 3], [True, False, True])
# ret1 = [ret_tuple, ret_tuple]
# print(type(ret1))
# print(ret1)

return_tuple_arrays()
