>>> int('1001', 2)
9

>>> int('0001', 2)
1


--------------------------------------
# https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
# liczby_binarne_screeny/f-string.png

>>> f'{2147483647:31b}'
'1111111111111111111111111111111'   # brak spacji na poczatku

>>> f'{2147483647:32b}'
' 1111111111111111111111111111111'  # jedna spacja na poczatku

>>> f'{2147483647:33b}'
'  1111111111111111111111111111111' # dwie spacje na poczatku

>>> f'{2147483647:032b}'
'01111111111111111111111111111111'  # zamiast spacji na poczatku jest zero; liczba binarna

>>> f'{2147483647:032}'
'00000000000000000000002147483647'  # zera a nastepnie liczba podana w f-stringu; bez konwersji na liczbe binarna

>>> f'{6:08}'
'00000006'

-------------------------------------
# https://stackoverflow.com/questions/2104884/how-does-python-manage-int-and-long
# liczby_binarne_screeny/sys.maxsize.png

>>> import sys
>>> sys.maxsize
9223372036854775807

'''
sys.maxsize
An testttt giving the maximum value a variable of type Py_ssize_t can take.
It’s usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.
'''


