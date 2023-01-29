------   Mutable vs Immutable   ---------

#https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/
#https://datagy.io/python-append-to-tuple/

lista = [1, 2, 3, 4, 5]
id_1 = id(lista)  # 140602217766016
lista.append(6)   # [1, 2, 3, 4, 5, 6]
id_2 = id(lista)  # 140602217766016
id_1 == id_2      # >>> True

tup = (1, 2, 3, 4)
id_1 = id(tup)   # 140602218231904
tup += (5,)      # (1, 2, 3, 4, 5)
id_2 = id(tup)   # 140602262060864
id_1 == id_2     # >>> False

lista = [5,6,7]
id_1 = id(lista)    # 140602218124224
lista += [8,9,10]   # [5, 6, 7, 8, 9, 10]
id_2 = id(lista)    # 140602218124224
id_1 == id_2        # >>> True
