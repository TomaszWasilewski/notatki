import math

round(4.2313)    round(4.7438)    round(4.6532, 2)    math.floor(7.88)    math.ceil(9.24)
>>> 4            >>> 5            >>> 4.65            >>> 7               >>> 10

max(1,2,3,4)     max([1,2,3,4])   min(1,2,3,4)        sum(1,2,3,4)        sum([1,2,3,4])
>>> 4            >>> 4            >>> 1               >>> TypeError       >>> 10

pow(4,3)  # >>> 4 do potęgi 3 (64)

44 % 3
# >>> 2  # 44-2=42 -> 42/3=14 -> 14*3+2 = 44

# floor division - //
47 / 6     # >>> 7.833333333333333
47 // 6    # >>> 7 

------------------------------------ STRING ------------------------------------

imie = 'Milosz'
len(imie)    'agata'.index('a')    imie[5]    imie.replace('M','T')  'xaxaxa'.replace('x', '0')
>>> 6        # >>> 0               >>> 'z'    >>> 'Tilosz'           >>> '0a0a0a'

'To jest moje zdanie '.replace(' ', '!!!', 1)  # param 'count' - jest kilka spacji, chcemy zrobić 'replace' na 1-wszej
>>> 'To!!!jest moje zdanie '

'Jana III'.find('III')
# >>> 5       - zwraca indeks na którym szukany napis się zaczyna

'Jana'.find('III')
# >>> -1      - jeżeli nie znajdzie szukanego napisu - zwróci -1 !!! ; ważne zastosowanie do kostruowania if-ów


imie += ' Nowak'        imie * 5                               'usa71Usa4uSAufhusa'.count('usa')
>>> 'Milosz Nowak'      >>> 'MiloszMiloszMiloszMiloszMilosz'   # >>> 2

'l' in imie     'A' in imie
# >>> True      # >>> False

'pies' + 'pies'[::-1]
# >>> 'piesseip'

# [start=0:stop=0:co ile]
# indeksowanie zaczyna się od 0 , nie od 1
# jezeli stop jest podany to ostatnia zwrocona wartosc to stop-1
nazwisko = 'Brzeczyszczykiewicz'
nazwisko[0:3]   nazwisko[:3]    nazwisko[1:7:2]    nazwisko[1:-2]           nazwisko[:-3:3]
>>> 'Brz'       >>> 'Brz'       >>> 'rez'          >>> 'rzeczyszczykiewi'   >>> 'Beyckw'

for n in imie:
    print(n)    # >>> M i l o s z

# string.join(iterable)    join-polaczyc
names = ['tom','jan','xin']   # może też być tupla ('tom','jan','xin')
''.join(names)    ' '.join(names)     'ZZZ'.join(names)
>>> 'tomjanxin'   >>> 'tom jan xin'   >>> 'tomZZZjanZZZxin'

names_dict = {'n1': 'tom','n2': 'jan','n3': 'xin'}
' '.join(names_dict)          ' '.join(names_dict.values())
>>> 'n1 n2 n3'                >>> 'tom jan xin'

# string.split()    split-rozdzielac
'Sadzonki kasztana'.split()    ==    'Sadzonki kasztana'.split(' ')
>>> ['Sadzonki', 'kasztana']
'Sadzonki kasztana'.split('a')
>>> ['S', 'dzonki k', 'szt', 'n', '']
# zwroc uwage na pusty string na koncu tabl.; zdanie do rozdzielenia mialo "a" na koncu
bool('Sadzonki kasztana'.split('a')[4])
>>> False      # pusty string ma wart.log. False
'To jest moje zdanie'.split(' ', 1)  # param 'maxsplit' - jest kilka spacji, chcemy zrobić 'split' na 1-wszej
>>> ['To', 'jest moje zdanie']
'To jest moje zdanie'.split(' ', 2)
>>> ['To', 'jest', 'moje zdanie']

nazwisko = 'Nowak'
'Dane: {} {}'.format(imie, nazwisko)
>>> 'Dane: Milosz Nowak'

f'imie: {imie},nazwisko: {nazwisko}'
>>> 'imie: Milosz,nazwisko: Nowak'

imie.startswith('M')     imie.endswith('o')
>>> True                 >>> False

imie.upper()             imie.lower()
# >>> 'MILOSZ'           # >>> 'milosz'

'a'.isupper()            'a'.islower()
# >>> False              # >>> True

# isalpha() returns True if all the characters are alphabet letters (a-z).
'AxxoLLigY'.isalpha()    '?xxoLLigY!'.isalpha()  'asnds7'.isalpha()
# >>> True               # >>> False             # >>> False

# a string is considered a valid identifier if it only contains
# alphanumeric letters (a-z) and (0-9),or underscores (_).
# Valid identifier cannot start with a number, or contain any spaces.
'Al3d__9G'.isidentifier()  '55Al3d__9G'.isidentifier()  'Al 3d__9G'.isidentifier()
# >>> True                 # >>> False                  # >>> False

# isalnum() returns True if all characters are alphanumeric,
# meaning alphabet letter (a-z) and numbers (0-9).
'abdsg'.isalnum()   '16218'.isalnum()   'sdhaj3526'.isalnum()  'sd_haj3526'.isalnum()
# >>> True          # >>> True          # >>> True             # >>> False

# isascii() checks whether the string contains ASCII characters
'night@123'.isascii()    ' '.isascii()   'ö'.isascii()      '°'.isascii()
# >>> True               # >>> True      # >>> False        # >>> False

'22'.isdigit()   # jest też metoda string.isnumeric() i string.isdecimal()
# >>> True

# -----  The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
# -----  characters (space is the default leading character to remove)
# string.strip(characters) 
# characters  -  Optional. A set of characters to remove as leading/trailing characters.
# ----- Leading characters occur at the start of the string (leftmost part of the string).
# ----- Trailing characters are those characters which occur at the end of the string (rightmost part of the string).

"     banana     ".strip()
# >>> 'banana'
"     ban  ana     ".strip()
# >>> 'ban  ana'
",,,,,rrttgg.....banana....rrr".strip(',.grt')
# >>> 'banana'
",,,,,rrttgg      .....banana....rrr".strip(',.grt')
# >>> '      .....banana'
",,,,,rrttgg      .....banana....rrr".strip(' ,.grt')     # jako argument do 'characters' została dodana spacja !
# >>> 'banana'


# ---    Snippet_1    ---
l1 = ['32\n', '43\n', '65\n', '34\n ', '99\n ', '55', '31']  # !!! '34\n ', '99\n '
l2 = ['32\n', '43\n', '65\n', '34\n', '99\n', '55', '49']    # !!! '34\n', '99\n'
l1 = [x.replace('\n', '') for x in l1]
l2 = [x.replace('\n', '') for x in l2]
print([x for x in l1 if x in l2])        # >>> ['32', '43', '65', '55'] !!! brak 34 i 99
print(len([x for x in l1 if x in l2]))   # >>> 4
l1 = [x.strip() for x in l1]
l2 = [x.strip() for x in l2]
print([x for x in l1 if x in l2])        # >>> ['32', '43', '65', '34', '99', '55']
print(len([x for x in l1 if x in l2]))   # >>> 6

# ---    Snippet_2    ---
>>> {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, ..., 'x': 0, 'y': 0, 'z': 0}

-------------------------------- LIST, TUPLE, SET --------------------------------

[1]*8    # >>> [1, 1, 1, 1, 1, 1, 1, 1]
[1,2]*8  # >>> [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
l1=[1,2,3]
l2=[4,5,6]
l1+l2    # >>> [1,2,3,4,5,6]

# [start=0:stop=0:co ile]
# indeksowanie zaczyna się od 0 , nie od 1
# jezeli stop jest podany to ostatnia zwrocona wartosc to stop-1
lista = [1,2,3,4,5,6,7]
lista[3:]             lista[2:5]          lista[:-4]           lista[::-3]
# >>> [4, 5, 6, 7]    # >>> [3, 4, 5]     # >>> [1, 2, 3]      # >>> [7, 4, 1]

lista = [True, (8), 'c', 20]

# extend(iterable)
lista.extend([5,6,7,8])                lista.extend(('a','d'))
>>> [True, (8), 'c', 20, 5, 6, 7, 8]   >>> [True, (8), 'c', 20, 'a', 'd']
dict = {'n1': 'tom','n2': 'jan','n3': 'xin'}
lista.extend(dict)                            lista.extend(dict.values())
>>> [True, (8), 'c', 20, 'n1', 'n2', 'n3']    >>> [True, (8), 'c', 20, 'tom', 'jan', 'xin']
lista_2 = ['test1', 'test2']
lista.extend(lista_2)
>>> [True, (8), 'c', 20, 'test1', 'test2']

lista.insert(0, False)           lista.insert(2, 500)           lista.append('t')
>>> [False, True, 8, 'c', 20]    >>> [True, 8, 500, 'c', 20]    >>> [True, (8), 'c', 20, 't']

del lista[0]              lista.remove('c')
>>> [8, 'c', 20]          >>> [True, (8), 20]

lista = [1,1,1,1,2,3]
lista.count(1)            len(lista)    [1,2,6,5,4,6,6,2,2].index(6)
>>> 4                     >>> 6         # >>> 2

name = 'ewa'
list(name)               list([1,2,3,4])
>>> ['e', 'w', 'a']      >>> [1, 2, 3, 4]

tupla = (1,2,3,4,5,6,7,8,9)
tupla[::-2]
>>> (9, 7, 5, 3, 1)

# set(lista) usuwa powtórzenia w liście
lista = [1,1,2,3,2,'g',4,5,5,5,4,'g']
set(lista)                  type(set(lista))     list(set(lista))
>>> {1, 2, 3, 4, 5, 'g'}    >>> <class 'set'>    >>> [1, 2, 3, 4, 5, 'g']

lista = [1,2,8,8,3,7,7,2,4,5,5,5]
lista.sort()
# >>> [1, 2, 2, 3, 4, 5, 5, 5, 7, 7, 8, 8]

# range(start=0, stop, step=1)
# ostatnia zwrocona wartosc to stop-1
list(range(10))
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(3,16,3))
# >>> [3, 6, 9, 12, 15]
test = range(1,21)
print(test)
# >>> range(1,21) - TO JEST GENERATOR

for index in range(len([5,6,7,8])):   # wyświetli indeksy; range(4)
    print(index)

for number in range(5):
    print(number)                     # >>> 0 1 2 3 4

for number in range(1,21):
    if number<=13 and number%2==0 and number!=10:
        print(number)                 # >>> 2 4 6 8 12

lista = [5,6,7]
for index, each in enumerate(lista):
    print(index, each)
>>> 0 5
>>> 1 6
>>> 2 7

l1 = [1,2,3]
l2 = ['a','b','c']
l3 = [7,8,9]
for number1, letter2, number3 in zip(l1,l2,l3):
    print(number1, letter2, number3)
>>> 1 a 7
>>> 2 b 8
>>> 3 c 9

# ------------- SNIPPET 1 ------------------

lista = list()
lista.extend(range(10))
lista.extend(range(20, 30))
lista
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# ------------- SNIPPET 2 ------------------
# Split string into 'n' equal parts
>>> s = 'SOSSOSSOSSOS'   # len(s) -> 12
>>> [s[idx: idx + 3] for idx in range(0, len(s), 3)]
['SOS', 'SOS', 'SOS', 'SOS']

------------------------------------- DICT -------------------------------------

kontakty = {
    'jan': 111111,
    'jacek': 222222
}
print(kontakty)   # >>> {'jan': 111111, 'jacek': 222222}
kontakty['jan'] = 333333
kontakty['ewa'] = 444444
print(kontakty)   # >>> {'jan': 333333, 'jacek': 222222, 'ewa': 444444}
kontakty['jan']   ==   kontakty.get('jan')       # >>> 111111
kontakty.keys()   # >>> dict_keys(['jan', 'jacek'])
kontakty.values() # >>> dict_values([111111, 222222])
kontakty.items()  # >>> dict_items([('jan', 111111), ('jacek', 222222)])
kontakty[0]       # >>> KeyError

for name in kontakty:    ==    for key in kontakty.keys():
    print(name)                    print(key)
>>> jan
>>> jacek

for value in kontakty.values():
    print(value)
>>> 111111
>>> 222222

for key, value in kontakty.items():
    print(key, value)
>>> jan 111111
>>> jacek 222222

'jan' in kontakty                      # >>> True
'jan' in kontakty.keys()               # >>> True
333333 in kontakty.values()            # >>> False
('jan', 111111) in kontakty.items()    # >>> True

del kontakty['jan']                    # >>> {'jacek': 222222}
'jan' in kontakty                      # >>> False

slownik = {
    'a':2,
    (1,2): 'super hubert',
    123: {'slownik wewn.': [1,2,3]}
}
slownik[123]['slownik wewn.'][2]
>>> 3

----- SNIPPET 1 -----
# https://www.geeksforgeeks.org/python-substring-key-match-in-dictionary/
# Substring Key match in dictionary
birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
   }
birthdays_dict.items()
# >>> dict_items([('Albert Einstein', '03/14/1879'), ('Benjamin Franklin', '01/17/1706')])
[val for key, val in birthdays_dict.items() if 'Einstein' == key.split(' ')[1]][0]
# >>> 03/14/1879

----- SNIPPET 2 -----
# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
# Sort Python Dictionaries by Key
time_dict = {
    'Introduction': 100.0,
    'Exercises': 340.0,
    'Break': 65.0,
    'Numbers and strings': 55.0
}
time_dict.keys()
# >>> dict_keys(['Introduction', 'Exercises', 'Break', 'Numbers and strings'
sorted_keys = list(time_dict.keys())
# ['Introduction', 'Exercises', 'Break', 'Numbers and strings']
sorted_keys.sort()
# ['Break', 'Exercises', 'Introduction', 'Numbers and strings']
sorted_time_dict = {k: time_dict[k] for k in sorted_keys} #  --->  Dictionary Comprehension
# {'Break': 65.0, 'Exercises': 340.0, 'Introduction': 100.0, 'Numbers and strings': 55.0}

----- SNIPPET 3 -----
# TODO
# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
# pozostałe przykłady sortowania

----------------------------------- FUNKCJE ------------------------------------

def dzialania(x,y):
    suma = x + y
    iloczyn = x * y
    return suma,iloczyn

print(dzialania(3,4))        # >>> (7, 12)
suma,iloczyn=dzialania(3,4)  # "PODWOJNE PRZYPISANIE"
print(suma,iloczyn)          # >>> 7 12

-------------------------------- *ARGS **KWARGS --------------------------------

# można podać dowolną ilość argumentów do funkcji
def suma(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

print(suma(1,2,3,4,5,6,7))
>>> 28


# tak samo jak dla *args tylko argumenty przyjmują formę słownika
def fun(**kwargs):
    print(kwargs)
    for kwarg_key, kwarg_value in kwargs.items():
        print(kwarg_key, kwarg_value)

fun(klucz_1='wartosc_a',klucz_2=222) # te argumenty będą słownikiem
>>> {'klucz_1': 'wartosc_a', 'klucz_2': 222}
>>> klucz_1 wartosc_a
>>> klucz_2 222

------------------------------------ LAMBDA ------------------------------------

def add(x):         ------>  lambda x: x+2
    return x+2

lambda x: x+2        # program nic nie zwroci ani nic nie wyswietli
print(lambda x: x+2) # >>> <function <lambda> at 0x7f55a9b67550>
add = lambda x: x+2
print(add(7))        # >>> 9
result = add(7)
print(result)        # >>> 9

raise_to_power = lambda x, y: x ** y
print(raise_to_power(6, 3))            # >>> 216

func_transformed = lambda x, y, z: (x ** y) - z
print(func_transformed(6, 3, 5))       # >>> 211

word_multipl = lambda word, num: word * num
print(word_multipl('hey', 5))          # >>> heyheyheyheyhey

def anonymous(n):                 # funkcja
  return lambda a : a * n         # a w środku funkcja anonimowa

doubler = anonymous(2)
tripler = anonymous(3)
quadrupler = anonymous(4)

print(doubler(11))        # >>> 22
print(tripler(11))        # >>> 33
print(quadrupler(11))     # >>> 44

# Dzięki map i filter możemy przekazać lambdzie więcej niż 1-ną wartość
# map - operatory arytmetyczne, zwroci liste tej samej dlugosci
# filter - operatory logiczne, moze zwrocic liste innej dlugosci
# dzieki map i filter mozemy wykonac operacje lambda na kilku wartosciach a nie na jednej
print(map(lambda x: x+2, [1,2,3]))         # >>> <map object at 0x7f55a87abfa0>
print(list(map(lambda x: x+2, [1,2,3])))   # >>> [3, 4, 5]
print(filter(lambda x: (x%2==0), [1,2,3])) # >>> <filter object at 0x7f55a2742670>
print(list(filter(lambda x: (x%2==0), [1,2,3])))   # >>> [2]

                                   --x--   --y--
print(list(map(lambda x, y: x * y, [3,4,5],[3,4,5])))                   # >>> [9,16,25]
                                            --x--   --y--   --z--
print(list(map(lambda x, y, z: (x * y) - z, [3,4,5],[3,4,5],[3,4,5])))  # >>> [6,12,20]

print(list(map(lambda x: x+'aaa', ['ala', 'basia', 'zosia'])))
# >>> ['alaaaa', 'basiaaaa', 'zosiaaaa']

print(list(filter(lambda x: len(x)>3, ['ala', 'basia', 'zosia'])))  # >>> ['basia', 'zosia']

def add_aa(napis):
    return len(napis)>3  # add_aa() zwraca True lub False
# w srodku lambdy mozemy umiescic funkcje
print(list(filter(lambda x: add_aa(x), ['ala', 'basia', 'zosia'])))
# ZWROCI ['basia', 'zosia'] , NIE ZWROCI [True, True]

import datetime
print(list(map(lambda date: datetime.datetime.strptime(date, '%d.%m.%Y %H:%M:%S'),
               ['25.08.1995 00:00:00', '22.07.1999 00:00:00'])))
# >>> [datetime.datetime(1995, 8, 25, 0, 0), datetime.datetime(1999, 7, 22, 0, 0)]

-------------------------------- LIST COMPREHENSION --------------------------------

[x for x in [1,2,3] if x%2==0]                 # W SRODKU FOR PO PRAWEJ IF
[x+1 for x in [1,2,3] if x%2==0]
[x for x in [1,2,3,4] if (x%2==0 and x>3)]
[x.replace('#','T') for x in ['#ttt','ala','zo#ia']]   # BEZ IF-A
[x for x in range(10)]                                 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[x for x in range(10,31) if '3' in str(x)]             # [13, 23, 30]
[index for index, x in enumerate([1,2,3]) if x%2==0]
[index for index, x in enumerate([1,2,3]) if not x%2==0]
[x+1 if x%2==0 else x for x in [1,2,3]]        # W SRODKU IF ELSE PO PRAWEJ FOR
[x+1 if x%2==0 else 'nie' for x in [1,2,3]]    # W SRODKU IF ELSE PO PRAWEJ FOR
[v1 if v1>v2 else v2 for v1,v2 in zip([1,4,2],[7,3,0])] # >>> [7, 4, 2]
[max(v1,v2) for v1,v2 in zip([1,4,2],[7,3,0])]          # >>> [7, 4, 2]

----------------------------------- PĘTLE ------------------------------------------

n = 6
while n>0:
    n -= 1
    if n == 2:
        continue
    print(n)
# często jest tak, że za pomocą zaprzeczenia możemy skrócić kod
# (porównaj poniższe z powyższym)
n = 6
while n>0:
    n -= 1
    if n != 2:
        print(n)

------------------------------------ REKURENCJA ------------------------------------

# w srodku funkcji jest wywolanie jej samej
# gdybysmy podali liczbe <0 funkcja dzialalaby w nieskonczonosc
def odliczanie(n):
    if n==0:
        print('koniec')
    else:
        print(n)
        odliczanie(n-1)

odliczanie(2)      # >>> 2 1 koniec
odliczanie(10)     # >>> 10 9 8 7 6 5 4 3 2 1 koniec

# --------------------------------- BUILT IN FUNCTIONS --------------------------------
'''
The map() function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter.

map(function, iterables) 
'''
def myfunc_1(n):
  return len(n) + 100

x = map(myfunc_1, ('metallica', 'pearl_jam', 'dire_straits'))
print(x)        # >>> <map object at 0x7f3a473acc10>
print(list(x))  # >>> [109, 109, 112]

def myfunc_2(a, b):
  return a % b

x = map(myfunc_2, (7, 17, 27), (3, 13, 23))
print(x)         # >>> <map object at 0x7f3a473c0df0>
print(list(x))   # >>> [1, 4, 4]

# ------------------------------------ RANDOM MODULE ------------------------------------

import random

# random.choice - wylosuje 1 element
print(random.choice([1,2,3,4,5,6,7,8]))
# random.choices - wylosuje "k" elementów, możliwe są powtórzenia
print(random.choices([1,2,3], k=2))    # >>> może być np.: [2,2]
# random.sample - wylosuje "k" elementów, nie będzie powtórzeń
print(random.sample([1,2,3], k=2))     # >>> na pewno nie będzie [2,2]

print(random.choices(range(1,11), k=5))    # >>> [3, 9, 6, 6, 2]

# losowanie na słowniku
dict = {1:'a',2:'b',3:'c',4:'d'}
random.sample(dict.items(), 2)         # >>> [(4, 'd'), (3, 'c')]

lista = [1,2,3,4,5,6,7,8]
# random.shuffle - miesza elementy na liście
random.shuffle(lista)
print(lista)           # >>> [1, 5, 3, 8, 7, 2, 4, 6]

# random.seed - jeżeli chcesz wygenerować za każdym razem tę samą liczbę gdy
# używasz dowolnej funkcji modułu random, musisz wywołać random.seed(seed value)
# z tym samym seed value przed każdym wywołaniem tej funkcji.
# Jako seed value podajemy dowolną liczbę.
# random.seed przydaje się gdy potrzebujesz PRZEWIDYWALNE ŹRÓDŁO LICZB LOSOWYCH.
random.seed(20)
random.randint(10,50)    # >>> 19
random.seed(30)
random.randint(10,50)    # >>> 44
random.seed(40)
random.randint(10,50)    # >>> 39
random.randint(10,50)    # >>> 47  nie było wywołania ziarna losowania
random.randint(10,50)    # >>> 43  nie było wywołania ziarna losowania
random.seed(30)
random.randint(10,50)    # >>> 44
random.seed(40)
random.randint(10,50)    # >>> 39
random.seed(20)
random.randint(10,50)    # >>> 19

for i in range(5):
    random.seed(25)
    print(random.choice(lista))  # >>> 6 6 6 6 6

--------------------------------- COLLECTIONS MODULE ---------------------------------

import collections
collections.Counter([1,2,6,5,4,6,6,2,2])      # zliczy wystąpienia wszystkich el.
# >>> Counter({2: 3, 6: 3, 1: 1, 5: 1, 4: 1})
[1,2,6,5,4,6,6,2,2].count(6)    # lista.count() zliczy wystąpienia tylko 1-go el.
# >>> 3
collections.Counter([1,2,6,5,4,6,6,2,2]).most_common()
# >>> [(2, 3), (6, 3), (1, 1), (5, 1), (4, 1)]
collections.Counter([1,2,6,5,4,6,6,2,2]).most_common(1)
# >>> [(2, 3)]
collections.Counter([1,2,6,5,4,6,6,2,2]).most_common(2)
# >>> [(2, 3), (6, 3)]

lista = ['ivan','gieorgij','sascha','ivan','gieorgij','misza','ivan',
         'nikita','vladimir','vladimir','gieorgij','gieorgij','gieorgij']
collections.Counter(lista)
# >>> Counter({'gieorgij': 5, 'ivan': 3, 'vladimir': 2, 'sascha': 1, 'misza': 1, 'nikita': 1})
collections.Counter(lista).most_common()
# >>> [('gieorgij', 5), ('ivan', 3), ('vladimir', 2), ('sascha', 1), ('misza', 1), ('nikita', 1)]
collections.Counter(lista).most_common(1)
# >>> [('gieorgij', 5)]
collections.Counter(lista).most_common(2)
# >>> [('gieorgij', 5), ('ivan', 3)]

c = Counter(['black','blue'])
c
# >>> Counter({'black': 1, 'blue': 1})
c.update({'red': 1, 'black': 8})  
c
# >>> Counter({'black': 9, 'blue': 1, 'red': 1})

# -------------------------
# WAŻNE ZASTOSOWANIE collections.Counter(): możemy jeden Counter poszerzyć o wartości drugiego Countera:
# PANDAS_CASE_STUDY.ipynb - Zadanie 11 (Sposób 2)

# TODO notatka o collections.OrderedDict

----------------------------------- ITERTOOLS MODULE -----------------------------------

import itertools
# product() zwraca iloczyn kartezjański podanych tablic
list(itertools.product(range(1,4), ['pik','karo','trefl']))
# >>> [(1, 'pik'), (1, 'karo'), (1, 'trefl'), (2, 'pik'), (2, 'karo'),
#      (2, 'trefl'), (3, 'pik'), (3, 'karo'), (3, 'trefl')]
list(itertools.product(range(1,4), ['pik','karo','trefl'], ['carlsen','romidiev']))
# >>> [(1, 'pik', 'carlsen'), (1, 'pik', 'romidiev'), (1, 'karo', 'carlsen'),
#      (1, 'karo', 'romidiev'), (1, 'trefl', 'carlsen'), (1, 'trefl', 'romidiev'),
#      (2, 'pik', 'carlsen'), (2, 'pik', 'romidiev'), (2, 'karo', 'carlsen'),
#      (2, 'karo', 'romidiev'), (2, 'trefl', 'carlsen'), (2, 'trefl', 'romidiev'),
#      (3, 'pik', 'carlsen'), (3, 'pik', 'romidiev'), (3, 'karo', 'carlsen'),
#      (3, 'karo', 'romidiev'), (3, 'trefl', 'carlsen'), (3, 'trefl', 'romidiev')]

# itertools.combinations()
from itertools import combinations 
letters ="GeEKS"
# size of combination is set to 3 
a = combinations(letters, 3)
a
# >>> <itertools.combinations object at 0x7f700510ef40>
# itertools.combinations zwraca iterator
next(a)
# >>> ('G', 'e', 'E')
next(a)
# >>> ('G', 'e', 'K')
next(a)
# >>> ('G', 'e', 'S')
list(a)
# >>> [('G', 'E', 'K'), ('G', 'E', 'S'), ('G', 'K', 'S'), ('e', 'E', 'K'), ('e', 'E', 'S'), ('e', 'K', 'S'), ('E', 'K', 'S')]
next(a)
# >>> StopIteration
# --------------------
a = combinations(letters, 3)
[x for x in a]
# >>> [('G', 'e', 'E'), ('G', 'e', 'K'), ('G', 'e', 'S'), ('G', 'E', 'K'), ('G', 'E', 'S'), ('G', 'K', 'S'), ('e', 'E', 'K'),
# >>>  ('e', 'E', 'S'), ('e', 'K', 'S'), ('E', 'K', 'S')]
# jeżeli np.: 'S' znajduję się za 'e' (w zm. letters) to nie znajdziemy kombinacji w której 'S' znajduje się PRZED 'e' itd.
# --------------------
a = combinations(letters, 3)
[' '.join(i) for i in a]
# >>> ['G e E', 'G e K', 'G e S', 'G E K', 'G E S', 'G K S', 'e E K', 'e E S', 'e K S', 'E K S']

----------------------------------- STATISTICS MODULE -----------------------------------

import statistics
# mean() liczy średnią arytmetyczną
statistics.mean([1,2,3,4,5,6])  # >>> 3.5

---------------------------------- WYRAŻENIA REGULARNE ----------------------------------

import re
punctuations = '!()-[]{};:\'"\,<>./?@#$%^&*_~'
# dzięki backslashowi po dwukropku, apostrof który jest po backslashu nie jest
# traktowany jako znak specjalny. Gdyby nie było backslasha, string kończyłby
# się na dwukropku, ponieważ znakiem rozpoczynającym i kończącym string
# jest tu apostrof
punctuations[0]   # >>> ' ! '
punctuations[-1]  # >>> ' ~ '
punctuations[9]   # >>> ' : '
punctuations[10]  # >>> " ' "
punctuations[11]  # >>> ' " '
punctuations[12]  # >>> ' \\ '
punctuations[13]  # >>> ' , '

# match() zwraca znaleziony napis, jeżeli znajduje sie on na początku
# stringa w którym go szukamy. W przeciwnym wypadku zwróci None.
re.match(r"napis", "napis tu jest napisany")
# >>> <re.Match object; span=(0, 5), match='napis'>
re.match(r"napis", "teraz napis tu jest napisany")   # >>> None

re.match(r"napis", "napis tu jest napisany").group() # >>> napis
re.match(r"napis", "teraz napis tu jest napisany").group()
# >>> AttributeError: 'NoneType' object has no attribute 'group'

# search() w przeciwieństwie do match() szuka patternu w całym stringu
# zwróci on pierwsze pojawienie sie patternu na jakie natrafi
re.search(r'kraj', 'Dziki kraj aborygenów')
# >>> <re.Match object; span=(6, 10), match='kraj'>
re.search(r'kraj', 'Dziki kraj aborygenów').group()  # >>> kraj

# "  .  " kropka oznacza dowolny znak, OPRÓCZ ZNAKU NOWEJ LINII
re.search(r'N.p.s', 'Napis').group()   # >>> Napis
re.search(r'N.p.s..', 'szukam N p5s!?;;; tutaj').group()   # >>> N p5s!?
re.search(r'N.p.s', 'Nop5x')           # >>> None
re.search(r'N.p.s..', 'szukam N\tp5s!?;;; tutaj').group()  # >>> N\tp5s!?
re.search(r'N.p.s..', 'szukam N\np5s!?;;; tutaj')          # >>> None

# "  ^  " kareta (caret) oznacza początek napisu
re.search(r'^Na.', 'Napis').group()       # >>> Nap
re.search(r'^Na.', 'Na jj Nal').group()   # >>> "Na '
re.search(r'^Na.', 'Teraz Napis tu')      # >>> None

# "  $  " dolar oznacza koniec napisu
re.search(r'Na.$', 'Napis')          # >>> None
re.search(r'Na$', 'isNap')           # >>> None
re.search(r'Na.$', 'isNap').group()  # >>> Nap

# "  *  " gwiazdka (asterisk) -
# - powtarza ostatni znak zero, raz lub wiele razy. !! moze nie byc ostatniego znaku w stringu w którym szukamy !!
re.search(r'^N*', 'N').group()             # >>> N
re.search(r'^N*', 'NNN').group()           # >>> NNN
re.search(r'^N*', '')
# >>> <re.Match object; span=(0, 0), match=''>
re.search(r'^Na*', 'N').group()            # >>> N
re.search(r'^Naa*', 'N')                   # >>> None
re.search(r'^Na*', 'Na').group()           # >>> Na
re.search(r'^Na*', 'Naa').group()          # >>> Naa
re.search(r'^Na*', 'Naaaaaaaaaaa').group() # >>> Naaaaaaaaaaa
re.search(r'^Na.*', 'Napis').group()       # >>> Napis
re.search(r'^Na.*', 'Na').group()          # >>> Na
re.search(r'^Na.*', 'Narrrrrrrr').group()  # >>> Narrrrrrr

# "  +  " plus - ostatni znak musi byc przynajmniej raz,
# może być też wiele razy
re.search(r'Na.*', 'Na').group()   # >>> Na
re.search(r'Na.+', 'Na')           # >>> None
re.search(r'Na.+', 'Naa').group()  # >>> Naa
re.search(r'Na.+', 'Napppp222????!!%%%').group()  # >>> Napppp222????!!%%%

# "  (...)  " szuka wyr. reg. zawartego w nawiasach
# "  \  " backslash zabiera specjalne działanie następującemu po nim znakowi,
# będzie on traktowany jako zwykły znak
re.search(r'\(.*\)', '(a) b (c)').group()     # >>> (a) b (c)
re.search(r'\(.*\)', 'aaa (a) b (c)').group() # >>> (a) b (c)
re.search(r'^\(.*\)', 'aaa (a) b (c)')        # >>> None
re.search(r'^\(.*\)', '(a) b (c)').group()    # >>> (a) b (c)
re.search(r'\(.*\)', '(a) b (c').group()      # >>> (a)
re.search(r'\(.\)', '(a) b (c)').group()      # >>> (a)
re.search(r'.*', '(a) b (c)').group()         # >>> (a) b (c)
re.search(r'(.*)', '(a) b (c)').group()       # >>> (a) b (c)
re.search(r'(.*)', '() b (c)').group()        # >>> () b (c)
re.search(r'(\(.\))', '() b (c)').group()     # >>> (c)

# "  ?  " znak zapytania ogranicza zakres do jak najmniejszego -
# - np. jeżeli następuje po "  +  " zadowoli się jednym znakiem,
# a jeżeli następuje po "  *  " zadowoli się brakiem znaku
re.search(r'Na*', 'Naaaaa').group()         # >>> Naaaaa
re.search(r'Na*?', 'Naaaaa').group()        # >>> N
re.search(r'Na+?', 'Naaaaa').group()        # >>> Na
re.search(r'a+?', 'Naaaaa').group()         # >>> a
re.search(r'a+', 'Naaaaa').group()          # >>> aaaaa
re.search(r'\(.*?', '(a) b (c)').group()    # >>> (
re.search(r'\(.*?\)', '(a) b (c)').group()  # >>> (a)
re.search(r'N*?', 'Naaaaa')                 # >>> <re.Match object; span=(0, 0), match=''>
string = 'Karol Kowalski, ul.Prosta 5/10, 675-835-578, 04-445'
re.search(r' ul\..+,',string).group()   # >>> ' ul.Prosta 5/10, 675-835-578,'
# dzięki "?" zatrzyma się po znalezieniu pierwszego przecinka
re.search(r' ul\..+?,',string).group()  # >>> ' ul.Prosta 5/10,'
re.search(r' ul\..+?',string).group()   # >>> ' ul.P'

# "  [...]  " w nawiasach kwadratowych znaki tracą specjalne działanie,
# między nawiasami podajemy zbiór znaków, możemy także zastosować
# zapis [v1-v2]: wówczas w zbiorze będą wszystkie znaki od value1
# do value2, możliwy jest też zapis [v1-v2v3-v4] - wówczas brane
# będą pod uwagę dwa zakresy: od v1 do v2 i od v3 do v4,
# omówienie zastosowań poniżej

# zwróci pierwszy znaleziony znak z zakresu [lj*?]
re.search(r'[lj*?]', '?hlj*?').group()      # >>> ?
re.search(r'[lj*?]', 'h*lj*?').group()      # >>> *
re.search(r'[lj*?]', '??jjj*h*f').group()   # >>> ?

# zwróci pierwszy znaleziony ciąg znaków z zakresu [lj*?]
# lub pierwszy znaleziony znak z tego zakresu
re.search(r'[lj*?]+', '?hlj*?').group()       # >>> ?
re.search(r'[lj*?]+', 'h??jjj*h').group()     # >>> ??jjj*

re.search(r'[a-c]', 'balabac').group()        # >>> b
re.search(r'[0-5]+', 'h??420351*h').group()   # >>> 420351
re.search(r'[k-o]+', 'h??jmmllnoookjj').group()  # >>> mmllnoook
re.search(r'[b-dg-i]+', '??ddcffihi').group() # >>> ddc
re.search(r'[b-dg-i]+', '??ddcihi').group()   # >>> ddcihi

# szuka stringa "lj*?" lub "lj*??.."
re.search(r'lj\*\?+', '?h*jl')                 # >>> None
re.search(r'lj\*\?+', 'hlj*??j').group()       # >>> lj*??
re.search(r'[abc]', 'falabac').group()         # >>> a
re.search(r'[abc]+', 'falabac').group()        # >>> a
re.search(r'[alh]', 'lahla').group()           # >>> l
re.search(r'[alh]+', 'iilahla').group()        # >>> lahla
re.search(r'[a-z]', 'falafel').group()         # >>> f
re.search(r'[a-z]', '645453??falafel').group() # >>> f
re.search(r'[a-z]+', 'falafel').group()        # >>> falafel
re.search(r'[a-z*]+', 'fala**fel').group()     # >>> fala**fel
re.search(r'[(+*)]+', 'ababa ((++ ababa ').group()          # >>> ((++
re.search(r'[0-9]+[a-z]+', '9573528hafdyusk94635').group()  # >>> 9573528hafdyusk
re.search(r'[0-9][a-z]+', '9573528hafdyusk94635').group()   # >>> 8hafdyusk
re.search(r'[c-d]+?', 'abccccc_abc').group()   # >>> c

# "  [^...]  "  - zastosowanie ^ w nawiasach kw. oznacza znak wykluczenia,
# a więc będziemy szukać wszystkiego poza tym znakiem / znakami

# [^512]jajko[^5]+  - wykluczamy 5,1,2 ale wciąż przed słowem 'jajko' musi
# pojawić się jeden znak z niewykluczonych, natomiast po słowie 'jajko'
# musi pojawić się jeden lub więcej znaków innych niż "5"
re.search(r'[^512]jajko[^5]+', '5512jajko67589')              # >>> None
re.search(r'[^512]jajko[^5]', '55123jajko589')                # >>> None
re.search(r'[^512]jajko[^5]', '5512334jajko67589').group()    # >>> 4jajko6
re.search(r'[^512]+jajko[^5]+', '5512334jajko67589').group()  # >>> 334jajko67
re.search(r'[^a-c0-2]+jajo', 'abc01277jajo66').group()        # >>> 77jajo
re.search(r'[^a-c0-2]jajo', '012abc77jajo66').group()         # >>> 7jajo

# Istnieją też skróty, które pozwalają nam wyszukiwać grupy znaków szybciej
#   \d - cyfry == [0-9]
#   \D - zaprzeczenie \d: litery, znaki specjalne, spacje, taby, nowe linie
#   \s - spacje, taby, nowe linie
#   \S - zaprzeczenie \s: litery, cyfry, znaki specjalne
#   \w - litery, cyfry, podkreślnik == [a-zA-Z0-9_] (te znaki nazywamy "word characters")
#   \W - zaprzeczenie \w: pozostałe znaki specjalne, spacje, taby, nowe linie
#   \b - samodzielne słowo (omówienie poniżej)

re.search(r'\d', 'aa123').group()             # >>> 1
re.search(r'\d+', 'bb12345##67').group()      # >>> 12345
re.search(r'\d+?', 'Warszawa++?*)%^&)234?').group()   # >>> 2
re.search(r'\D', '12345##67').group()         # >>> #
re.search(r'\D+', 'Warszawa++?*)%^&)234??').group()   # >>> Warszawa++?*)%^&)
re.search(r'\D+', '55b!@?\tb #\nt__12345##67').group()
# >>> b!@?	b #
# >>> t__

re.search(r'\s', '56__!!hhgh%%')    # >>> None
re.search(r'\s', '56 hhgh%%')       # >>> <re.Match object; span=(2, 3), match=' '>
re.search(r'\s', '56h\thgh%%')      # >>> <re.Match object; span=(3, 4), match='\t'>
re.search(r'\s', '56h\nhgh%%')      # >>> <re.Match object; span=(3, 4), match='\n'>
re.search(r'\s+', '56h\t  \nhgh%%') # >>> <re.Match object; span=(3, 7), match='\t  \n'>
re.search(r'\s+', 'Warszawa        to piekne miasto')
# >>> <re.Match object; span=(8, 16), match='        '>

re.search(r'\S', 'Warszawa*(& to piekne miasto').group()        # >>> W
re.search(r'\S', ' 55 Warszawa*(& to piekne miasto').group()    # >>> 5
re.search(r'\S+', 'Warszawa*(& to piekne miasto').group()       # >>> Warszawa*(&
re.search(r'\S+', '\t Wars334&zawa to piekne miasto').group()   # >>> Wars334&zawa

re.search(r'\w', '## Warszawa to piekne miasto').group()             # >>> W
re.search(r'\w+', '?5__Warszawa to piekne miasto').group()           # >>> 5__Warszawa
re.search(r'\w+', '\nWar&szawa to piekne miasto').group()            # >>> War
re.search(r'[a-z0-9_]+', '?5__Warszawa to piekne miasto').group()    # >>> 5__
re.search(r'[a-zA-Z0-9]+', '?5__Warszawa to piekne miasto').group()  # >>> 5
re.search(r'[a-zA-Z0-9_]+', '?5__Warszawa to piekne miasto').group() # >>> 5__Warszawa
re.search(r'\W', 'War__&#!szawa to piekne miasto').group()           # >>> &
re.search(r'\W+', 'War__&  #\t!$%~\n) )szawa miasto').group()
# >>> &  #	!$%~
# >>> ) )

# \b szuka "samodzielnego słowa"
# \b "akceptuje" znaki z grupy: \W
# \b "nie akceptuje" znaków z grup: \w
re.findall(r'tak', 'taktaktaktak')       # >>> ['tak', 'tak', 'tak', 'tak']
re.findall(r'\btak', 'taktaktaktak')     # >>> ['tak']
re.findall(r'\btak', ' taktaktaktak')    # >>> ['tak']
re.findall(r'\btak', '.taktaktaktak')    # >>> ['tak']
re.findall(r'\btak', '(#)taktaktaktak')  # >>> ['tak']
re.findall(r'\btak', 'xtaktaktaktak')    # >>> []
re.findall(r'\btak', '3taktaktaktak')    # >>> []
re.findall(r'\btak', '_taktaktaktak')    # >>> []
re.findall(r'\b_34tak', '!!_34taktaktaktak')  # >>> ['_34tak']
re.findall(r'\b_34tak', '___34taktaktaktak')  # >>> []

re.findall(r'tak', 'taktaktaktak')       # >>> ['tak', 'tak', 'tak', 'tak']
re.findall(r'tak\b', 'taktaktaktak')     # >>> ['tak']
re.findall(r'tak\b', 'taktaktaktak ')    # >>> ['tak']
re.findall(r'tak\b', 'taktaktaktak\n')   # >>> ['tak']
re.findall(r'tak\b', 'taktaktaktak\t')   # >>> ['tak']
re.findall(r'tak\b', 'taktaktaktak???')  # >>> ['tak']
re.findall(r'tak\b', 'taktaktaktakxx')   # >>> []
re.findall(r'tak\b', 'taktaktaktak33')   # >>> []
re.findall(r'tak\b', 'taktaktaktak__')   # >>> []

re.findall(r'\btak\b', '!!taktaktaktak??')      # >>> []
re.findall(r'\btak\b', '!!tak tak_tak\ntak??')  # >>> ['tak', 'tak']
re.findall(r'\bma\b', 'mama ma kota i malujema kota')  # >>> ['ma']
re.findall(r'\bma\b', 'mama ma kota i maluje.ma kota') # >>> ['ma', 'ma']

re.findall(r'\bma', 'mama ma kota i maluje.ma kota')
# >>> ['ma', 'ma', 'ma', 'ma']
re.findall(r'ma\b', 'mama ma kota i maluje.ma kota')
# >>> ['ma', 'ma', 'ma']
re.findall(r'\w+a\b', 'Balbina,Tomasz,Barbara,Beata,Błażej,Agata?Magda')
# >>> ['Balbina', 'Barbara', 'Beata', 'Agata', 'Magda']

re.findall(r'\b\d{2}-\d{3}', '022-081')               # >>> []
re.findall(r'\d{2}-\d{3}\b', '022-081xx')             # >>> []
re.findall(r'\b\d{2}-\d{3}\b', '73-110 _#22-081??')   # >>> ['73-110', '22-081']

# "  {m}  " oznacza ile powtórzeń danego znaku chcemy
re.search(r'\d{2}-\d{3}', '02-081').group()     # >>> 02-081
re.search(r'\d{2}-\d{3}', '022-081').group()    # >>> 22-081

# "  {m,n}  " określa dokładny zakres ilości powtórzeń
# {m,n} - zakres od m do n
# {m,}  - zakres od m do nieskończenie wielu
# {,n}  - zakres od 0 (może nie być znaku) do n
# {,}   - zakres od 0 (może nie być znaku) do nieskończenie wielu
re.search(r'\d{3,4}-\d{3}', '02-081')             # >>> None
re.search(r'\d{4,}-\d{3}', '022-081')             # >>> None
re.search(r'\d{3,4}-\d{3}', '022-081').group()    # >>> 022-081
re.search(r'\d{3,4}-\d{3}', '0228-081').group()   # >>> 0228-081
re.search(r'\d{4,}-\d{3}', '0228-081').group()    # >>> 0228-081
re.search(r'\d{4,}-\d{3}', '0228977-081').group() # >>> 0228977-081
re.search(r'\d{,3}-\d{3}', '022-081').group()     # >>> 022-081
re.search(r'\d{,3}-\d{3}', '0224-081').group()    # >>> 224-081
re.search(r'\d{,3}-\d{3}', '-081').group()        # >>> -081
re.search(r'\d{1,3}-\d{3}', '-081')               # >>> None
re.search(r'\d{,}-\d{3}', '-081').group()         # >>> -081
re.search(r'\d{,}-\d{3}', '02289772-081').group() # >>> 02289772-081

re.search(r'\d+\+\d+', '22+2').group()  # >>> 22+2
re.search(r'\d+\*\d+', '2*2').group()   # >>> 2*2
re.search(r'\d+\+\d+', '+2')            # >>> None
re.search(r'\d+\*\d+', '2*')            # >>> None
re.search(r'\d+[+]\d+', '22+2').group() # >>> 22+2
re.search(r'\d+[*]\d+', '2*2').group()  # >>> 2*2

re.search(r'a{3}', 'ggyy56aaa23').group()         # >>> aaa
re.search(r'a{2,4}', 'ggyy56a23')                 # >>> None
re.search(r'a{2,4}', 'ggyy56aaaa23').group()      # >>> aaaa
re.search(r'a{,2}ggy', 'aaaaggyy56').group()      # >>> aaggy
re.search(r'a{,}ggy', 'bbggyy56').group()         # >>> ggy
re.search(r'[abc]{1,3}ggy', 'bbggyy56').group()   # >>> bbggy
re.search(r'[abc]{1,3}ggy', 'bacggyy56').group()  # >>> bacggy
re.search(r'[abc]{1,3}ggy', 'bacddggyy56')        # >>> None
re.search(r'[a-e]{,3}ggy', '55ggyy56').group()    # >>> ggy
re.search(r'[a-e]{,3}ggy', 'eacggyy56').group()   # >>> eacggy
re.search(r'a{1,3}', 'ggyy56aaa23').group()       # >>> aaa
re.search(r'a{1,3}?', 'ggyy56aaa23').group()      # >>> a

# "  |  "  - oznacza "lub"
re.search(r'War|Kra', 'wiem że Krakow to miasto').group()             # >>> Kra
re.search(r'[^512]+War|[^a-c0-2]Kra', 'wiem że bbKrakow to miasto')   # >>> None
re.search(r'[^512]+War|[^a-c0-2]Kra', 'bbJJKrakow to miasto').group() # >>> JKra
re.search(r'[^512]+War|[^a-c0-2]Kra', '533War i bbJJKrakow').group()  # >>> 33War

# findall() znajduje wszystkie dopasowania
re.findall(r'\w', 'W55__arszawa ??')
# >>> ['W', '5', '5', '_', '_', 'a', 'r', 's', 'z', 'a', 'w', 'a']
re.findall(r'\w+', 'W55__arszawa to pie\nkne mi asto')
# >>> ['W55__arszawa', 'to', 'pie', 'kne', 'mi', 'asto']
re.findall(r'\w+', '???')
# >>> []
re.findall(r'[^512]+War|[^a-c0-2]Kra', '533War i bbJJKrakow')
# >>> ['33War', 'JKra']
re.findall('[^\d][a-z]+', '_test 98041test23567_test')
# >>> ['_test', 'test', '_test']
re.findall(r'[a-e]{,3}ggy', '55ggyy5bcdeggy6bbggyyxx')
# >>> ['ggy', 'cdeggy', 'bbggy']
re.findall(r'\w{2,3}', '5__arszawa to pie\nkne mi asto')
# >>> ['5__', 'ars', 'zaw', 'to', 'pie', 'kne', 'mi', 'ast']
re.findall(r'\w{2,3}?', '5__arszawa to pie\nkne mi asto')
# >>> ['5_', '_a', 'rs', 'za', 'wa', 'to', 'pi', 'kn', 'mi', 'as', 'to']

# 'gdzie'.replace('co', 'na co')
'mam kotra, kotra mam'.replace("kotra", "kota")
# >>> mam kota, kota mam

# sub() pozwala zamienić string na inny string (podobnie jak replace)
# re.sub('co', 'na co', 'gdzie')
re.sub(r'\w+', 'zmieniony', 'Warszawa to piekne miasto &&??')
# >>> zmieniony zmieniony zmieniony zmieniony &&??
re.sub(r'\w+', 'zmieniony', 'Warszawa to piekne miasto &&??', count=2)
# >>> zmieniony zmieniony piekne miasto &&??
re.sub(r'\d{2}-\d{3}', 'kod-pocztowy', 'ww2-5ii33-30oo-rr73-110pp 88-900waw7-772yy')
# >>> ww2-5ii33-30oo-rrkod-pocztowypp kod-pocztowywaw7-772yy
re.sub(r'\d{2}-\d{3}', 'kod-pocztowy', 'ww33-33oo2-2')
# >>> ww33-33oo2-2

# (...)(...) , \1\2 
# wyrażenia w nawiasach stanowią grupy. poprzez "\1\2" odwołuję się do tych grup; pomiędzy grupami dojdzie spacja !!!
re.sub(r'(UL.)(\w)', r'\1 \2', 'UL.Zygmunta')   # po 'UL.' nie ma spacji
# >>> 'UL. Zygmunta'    (po 'UL.' jest spacja, bo dodałem spację między "\1" i "\2")

# TODO
# (?P<name>...) - nadawanie nazw grupom

# "  <string>(?=...)  " poszuka stringa PO KTÓRYM NASTĘPUJE WYRAŻENIE "..."
# ten pattern nazywamy "lookahead assertion"
re.search(r'ser (?=\d{3})', 'g ser 555').group()        # >>> 'ser '
re.search(r'ser (?=\d{3})', 'g ser 5')                  # >>> None
re.search(r'ser (?=\d{3,5})', 'g ser 55588').group()    # >>> 'ser '
re.search(r'ser(?=\w{1,3}.)', 'g serot_?').group()      # >>> ser
re.search(r'ser(?=\w{1,3}.)', 'g seraaaaaaaa').group()  # >>> ser
re.search(r'ser(?=\w+)', 'g serot_?').group()           # >>> ser
re.search(r'ser(?=\w{1,3}.\b)', 'g seraaaaaaaa')        # >>> None
re.search(r'ser(?=\w{1,3}.\b)', 'g seraaaa#').group()   # >>> ser

# "  <string>(?!...)  " poszuka stringa po którym NIE NASTĘPUJE wyrażenie "..."
# ten pattern nazywamy "negative lookahead assertion"
re.search(r'ser(?!\w)', 'g ser33')                 # >>> None
re.search(r'ser(?!\w)', 'g ser 33').group()        # >>> ser
re.search(r'ser(?!\d)', 'g ser 33').group()        # >>> ser
re.search(r'ser(?!\d)', 'g ser33')                 # >>> None
re.search(r'ser(?!\d{3,4})', 'g ser 555').group()  # >>> ser
re.search(r'ser(?!\d{3,4})', 'g ser5555')          # >>> None
re.search(r'ser(?!\d{3,4})', 'g ser55555')         # >>> None
re.search(r'ser(?!\d{3,4})', 'g ser55').group()    # >>> ser
re.search(r'\w+(?!\W)', '??f647%@&').group()       # >>> f64

# "  (?<=...)<string>  " poszuka stringa PRZED KTÓRYM NASTĘPUJE WYRAŻENIE "..."
# ten pattern nazywamy "positive lookbehind assertion"
re.search(r'(?<=abc)def', 'abcdef').group()    # >>> def
re.search(r'(?<=abc)def', 'abdef')             # >>> None
re.search(r'(?<=\d{3})def', '344def').group()  # >>> def
re.search(r'(?<=\d{3})def', 'g46def')          # >>> None
# w lookbehind assertion nie można podawać zakresów
re.search(r'(?<=\d{3,5})def', '2246def')
# >>> re.error look-behind requires fixed-width pattern
re.search(r'(?<=\d*)def', '2246def')
# >>> re.error ...
re.search(r'(?<=\d+)def', '2246def')
# >>> re.error ...

# "  (?<!...)<string>  " poszuka stringa przed którym NIE NASTĘPUJE wyrażenie "..."
# ten pattern nazywamy "negative lookbehind assertion"
re.search('(?<!\d)[a-z]+', '22abcdef').group()     # >>> bcdef
re.search('(?<!\d)[a-z]+', '567abc').group()       # >>> bc
re.findall('(?<!\d)[a-z]+', '22abcdef 567abc')     # >>> ['bcdef', 'bc']
re.search('(?<!\d{3})[a-z]+', '567abc').group()    # >>> bc
re.search('(?<!\d{3})[a-z]+', '67abc').group()     # >>> abc
re.search('(?<!\d{3})[a-z]+', '5675abc').group()   # >>> bc
re.search('(?<!\d{3,5})[a-z]+', '5675abc').group() # >>> re.error (patrz wyżej)

# możemy w jednym wyrażeniu zawrzeć lookbehind i lookahead assertion
re.search(r'(?<!\W)\w+(?!\W)', '??f647%@&').group()    # >>> 64

# ---    Snippet_1    ---
[re.sub(r'\n', '', x) for x in ['Darth\n', 'Luke\n', 'Darth\n']]
# >>> ['Darth', 'Luke', 'Darth']

# ---    Snippet_2    ---
# Time between range
logs = [
 '127.0.0.1 - - [10/Apr/2007:10:39:11 +0300]',
 '127.0.0.1 - - [10/Apr/2007:10:54:08 +0300]',
 '127.0.0.1 - - [10/Apr/2007:10:53:10 +0300]',
 '127.0.0.1 - - [10/Apr/2007:10:45:08 +0300]',
 '127.0.0.1 - - [10/Apr/2007:10:42:10 +0300]'
 ]
time_with_10_4 = [re.search(r'^127\.0\.0\.1\b.+10:4.+', log) for log in logs]  # time btw 10:40 and 10:50
# >>> [None, None, None, <re.Match object; span=(0, 42), match='127.0.0.1 ...]
time_with_10_4 = [time.group() for time in time_with_10_4 if time]
# >>> ['127.0.0.1 - - [10/Apr/2007:10:45:08 +0300]', '127.0.0.1 - - [10/Apr/2007:10:42:10 +0300]']
time_with_10_5 = [re.search(r'^127\.0\.0\.1\b.+10:5[01234].+', log) for log in logs]  # time btw 10:50 and 10:55
# >>> [None, <re.Match object; span=(0, 42), match='127.0.0.1 ...]
time_with_10_5 = [time.group() for time in time_with_10_5 if time]
# >>> ['127.0.0.1 - - [10/Apr/2007:10:54:08 +0300]', '127.0.0.1 - - [10/Apr/2007:10:53:10 +0300]']

# ---    Snippet_3    ---
# Handling long raw strings
new_string = (
    r"$VAR1 = { 'change1' => { 'change2' => 'change3', 'change4' => 'change5' },"
    '\n'
    r"'change6' => { 'change7' => 'change8', 'change9' => 'change*' } }"
)
# >>> $VAR1 = { 'change1' => { 'change2' => 'change3', 'change4' => 'change5' },
# >>> 'change6' => { 'change7' => 'change8', 'change9' => 'change*' } }
------------------------------------ DATETIME MODULE ------------------------------------

# ! datetime objects are immutable !
import datetime

# ---    datetime.time object    ---
"3 hours, 45 minutes, 30 seconds and 20 microseconds"
datetime.time(3, 45, 30, 20)
# >>> datetime.time(3, 45, 30, 20)
print(datetime.time(3, 45, 30, 20))
# >>> 03:45:30.000020
type(datetime.time(3, 45, 30, 20))
# >>> <class 'datetime.time'>

# ---    datetime.date object    ---
datetime.date(2014, 1, 10)
# >>> datetime.date(2014, 1, 10)
print(datetime.date(2014, 1, 10))
# >>> 2014-01-10
type(datetime.date(2014, 1, 10))
# >>> <class 'datetime.date'>

# ---    datetime.datetime object    ---
datetime.datetime(2020,12,24)
# >>> datetime.datetime(2020, 12, 24, 0, 0)
print(datetime.datetime(2020,12,24))
# >>> 2020-12-24 00:00:00
print(datetime.datetime(2020,12,24,13,10,5,300))
# >>> 2020-12-24 13:10:05.000300
type(datetime.datetime(2020,12,24))
# >>> <class 'datetime.datetime'>

# ---    attributes of datetime.datetime objects    ---
datetime.datetime.hour
# >>>    <attribute 'hour' of 'datetime.datetime' objects>
now = datetime.datetime(2020, 12, 2, 12, 27, 47, 52102)
type(now)        # >>> <class 'datetime.datetime'>
now.year         # >>> 2020
now.month        # >>> 12
now.day          # >>> 2
now.hour         # >>> 12
now.minute       # >>> 27
now.second       # >>> 47
now.microsecond  # >>> 52102
# część z atr. można używać na obiektach
# datetime.time lub datetime.date

# ---    datetime.datetime.now() method    ---
datetime.datetime.now()
# >>> datetime.datetime(2020, 11, 30, 18, 25, 30, 66375)
print(datetime.datetime.now())
# >>> 2020-11-30 18:21:45.646834
type(datetime.datetime.now())
# >>> <class 'datetime.datetime'>

# ---    datetime.datetime.isoweekday() method    ---
# ---    datetime.date.isoweekday() method    ---
now = datetime.datetime.now()
now.isoweekday()               # >>> 3 (środa)
past = datetime.date(2014, 1, 10)
past.isoweekday()              # >>> 5 (piątek)

# ---    datetime.datetime.timetuple() method    ---
# ---    datetime.date.timetuple() method    ---
# przykład_1
now = datetime.datetime.now()
now # >>> datetime.datetime(2020, 12, 2, 14, 54, 27, 665892)
now.timetuple()
# >>> time.struct_time(tm_year=2020, tm_mon=12, tm_mday=2,
# >>>                  tm_hour=14, tm_min=54, tm_sec=27,
# >>>                  tm_wday=2, tm_yday=337, tm_isdst=-1)
now.timetuple().tm_mday # >>> 2 (month's day)
now.timetuple().tm_wday # >>> 2 (week's day - range [0, 6], Monday is 0)
now.timetuple().tm_yday # >>> 337 (year's day)
# przykład_2
past = datetime.date(2014, 4, 27)
past # >>> datetime.date(2014, 4, 27)
past.timetuple()
# >>> time.struct_time(tm_year=2014, tm_mon=4, tm_mday=27,
# >>>                  tm_hour=0, tm_min=0, tm_sec=0,
# >>>                  tm_wday=6, tm_yday=117, tm_isdst=-1)
past.timetuple().tm_yday   # >>> 117

#  Konwersja stringów i dat
#  %Y - year
#  %d - day
#  %m - month
#  %H - hour
#  %M - minute
#  %S - second
#  ------------------------
#  %B - month's full name
#  %b - month's abbreviated name (abbreviate - skracać)
#  %A - weekday's full name
#  %I - Hour (12-hour clock)
#  %p - equivalent of either AM or PM
#  ------------------------
#  %z - UTC offset (+0000, -0400, +0300 ... itd.) offset - przesunięcie

# ---    datetime.datetime.strptime() method    ---
# datetime.datetime.strptime(date_string, format) -
# - string parsuj na datetime.datetime
# date_string i format muszą mieć tę samą składnię
date_str =  "01-10-2015T14:34"
print(datetime.datetime.strptime(date_str,"%m-%d-%YT%H:%M"))
# >>> 2015-01-10 14:34:00
type(datetime.datetime.strptime(date_str,"%m-%d-%YT%H:%M"))
# >>> <class 'datetime.datetime'>
date_str = "10/01/2015"
print(datetime.datetime.strptime(date_str,"%d/%m/%Y"))
# >>> 2015-01-10 00:00:00
date_str = 'Jan 20, 2017 5pm'
print(datetime.datetime.strptime(date_str, '%b %d, %Y %I%p'))
# >>> 2017-01-20 17:00:00
print(datetime.datetime.strptime('09:20', '%H:%M'))
# # nie musisz podawać daty, konsola nie wyświetli błędu, wyświetli np.: '1900-01-01 09:20:00'
# >>> datetime.datetime(1900, 1, 1, 9, 20)

# ---    datetime.datetime.strftime() method    ---
# datetime.datetime.strftime() - string from datetime.datetime
date = datetime.datetime(2020, 11, 30, 20, 48, 3)
date.strftime("%H:%M:%S %m-%d-%Y")
# >>> '20:48:03 11-30-2020'
type(date.strftime("%H:%M:%S %m-%d-%Y"))
# >>> <class 'str'>
# można też zapisać tak:
datetime.datetime.strftime(date, "%H:%M:%S %m-%d-%Y")
# >>> '20:48:03 11-30-2020'

# ---    datetime.timedelta object    ---
delta = datetime.timedelta(days=30, seconds=50,
                           microseconds=254768,
                           milliseconds= 657,
                           minutes=54, hours=10, weeks=4)
delta # >>> datetime.timedelta(days=58, seconds=39290, microseconds=911768)
type(delta) # >>> <class 'datetime.timedelta'>
datetime.timedelta.days  # >>> <member 'days' of 'datetime.timedelta' objects>
delta.days          # >>> 58
delta.seconds       # >>> 39290
delta.microseconds  # >>> 911768

# ---    datetime.timedelta.total_seconds() method    ---
delta = datetime.timedelta(days=30, seconds=50, microseconds=432098)
delta.total_seconds()     # >>> 2592050.432098

# ---    ILE CZASU ZOSTAŁO DO WYDARZENIA ?    ---
# ---    JAKI JEST ODSTĘP CZASU POMIĘDZY DATAMI ?    ---
# przykład_1
now = datetime.datetime.now()
christmas = datetime.datetime(2020,12,24)
difference = christmas-now
difference
# >>> datetime.timedelta(days=22, seconds=57378, microseconds=536162)
type(difference)            # >>> <class 'datetime.timedelta'>
print(difference)           # >>> 22 days, 15:56:18.536162 (tyle czasu zostało)
difference.total_seconds()  # >>> 1958178.536162
# przykład_2
datetime.date(2014, 10, 10) - datetime.date(2014, 1, 15)
# >>> datetime.timedelta(days=268)

# ---    DODAJMY LUB ODEJMIJMY OD DATY DNI    ---
# przykład_1
now = datetime.datetime.now()
offset = datetime.timedelta(days=45, hours=13)
now+offset
# >>> datetime.datetime(2021, 1, 15, 21, 3, 41, 463838)
type(now+offset)
# >>> <class 'datetime.datetime'>
print(now+offset)
# >>> 2021-01-15 21:03:41.463838
print(now-offset)
# >>> 2020-10-16 19:03:41.463838
offset_minus = datetime.timedelta(days=-45, hours=-13)
print(now+offset_minus)
# >>> 2020-10-16 19:03:41.463838
# przykład_2
datetime.date(2019, 6, 14) + datetime.timedelta(4)
# >>> datetime.date(2019, 6, 18)

# ---    datetime_object.replace() function ---
now = datetime.datetime.now()
# datetime.datetime(2023, 1, 17, 12, 25, 10, 65746)
now.replace(year=1998, hour=17)
# >>> datetime.datetime(1998, 1, 17, 17, 25, 10, 65746)
now
# >>> datetime.datetime(2023, 1, 17, 12, 25, 10, 65746)  datetime objects are immutable
new_date = now.replace(year=1998, hour=17)
# datetime.datetime(1998, 1, 17, 17, 25, 10, 65746)

# ---    Snippet_1    ---
lista = [datetime.datetime(1995, 8, 25, 0, 0), datetime.datetime(1999, 7, 22, 0, 0)]
min(lista)    # >>> datetime.datetime(1995, 8, 25, 0, 0)
max(lista)    # >>> datetime.datetime(1999, 7, 22, 0, 0)

# ---    Snippet_2    ---
now = datetime.datetime.now()
print(f'{now.year}-{now.month}-{now.day}')      # >>> 2020-11-30

# ---    Snippet_3    ---
# poniższy kod zwraca to samo co datetime.timedelta.total.seconds()
now = datetime.datetime.now()
christmas = datetime.datetime(2020,12,24)
difference = christmas-now
type(difference)         # >>> <class 'datetime.timedelta'>
difference.days*24*60*60 + difference.seconds   # >>> 1958178

# ---    Snippet_4    ---
[(datetime.date(2019, 6, 14) + datetime.timedelta(i)) for i in range(3)]
# >>> [datetime.date(2019, 6, 14), datetime.date(2019, 6, 15), datetime.date(2019, 6, 16)]

# ---    Snippet_5    ---
[datetime.datetime.strptime(date, '%d.%m.%Y %H:%M:%S') for date
    in ['25.08.1995 00:00:00', '22.07.1999 00:00:00']]
# >>> [datetime.datetime(1995, 8, 25, 0, 0), datetime.datetime(1999, 7, 22, 0, 0)]

--------------------------------- PYTHON-DATEUTIL MODULE ---------------------------------

# instalując posłużymy się komendą "pip install python-dateutil"
# gdy wyświetlimy moduły komendą "pip3 freeze" znajdziemy moduł "python-dateutil"
# !!!  jednak w kodzie nie zapiszemy:                   !!!
# !!!  import python-dateutil   lecz  import dateutil   !!!

from dateutil.parser import parse
# szybkie parsowanie stringa na obiekt datetime
# dzięki tej metodzie nie musimy przejmować się formatem stringa
print(parse('January 31, 2010'))        # >>> 2010-01-31 00:00:00
type(parse('January 31, 2010'))         # >>> <class 'datetime.datetime'>
print(parse('31 January, 2010'))        # >>> 2010-01-31 00:00:00
print(parse('2020 03 January'))         # >>> 2020-01-03 00:00:00
print(parse("2003-09-25T10:49:41"))     # >>> 2003-09-25 10:49:41
type(parse("2003-09-25T10:49:41"))      # >>> <class 'datetime.datetime'>
print(parse("2003-09-25 T 10:49:41"))   # >>> 2003-09-25 10:49:41
print(parse("10/01/2015"))              # >>> 2015-10-01 00:00:00

-------------------------------- CALENDAR MODULE ---------------------------------------------

from calendar import monthrange
# calendar.monthrange(year, month)
    # Returns weekday of first day of the month and number of days in month, for the specified year and month.
monthrange(2023, 1)
# >>> (6, 31)

