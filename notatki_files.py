# -- 1 --
f = open("my_file.txt", "w")  # ścieżka względna, jeżeli plik o takiej nazwie nie istnieje to zostanie stworzony
for i in range(10):
    f.write(f"This is line {i}")
f.close()
# my_file.txt
# This is line 0This is line 1This is line 2...

f = open("my_file.txt", "r")
contents = f.read()
f.close()
print(type(contents))
print(contents)
# >>> <class 'str'>
# >>> This is line 0This is line 1This is line 2

# -- 2 --
f = open("/home/wasil/Pulpit/Kurs_DS_2022/zjazd_2/bootcamp_2_zjazd/my_file.txt", "w")  # ścieżka bezwzględna
for i in range(10):
    f.write(f"This is line {i}\n")
f.close()
# my_file.txt
# This is line 0
# This is line 1
# This is line 2

f = open("my_file.txt", "r")
contents = f.read()
f.close()
print(type(contents))
print(contents)
# >>> <class 'str'>
# >>> This is line 0
# >>> This is line 1
# >>> This is line 2


# -- 3 --
lines = [f"This is line {i}" for i in range(10)]
print(lines)
# >>> ['This is line 0', 'This is line 1', 'This is line 2', ...]

f = open("my_file.txt", "w")
f.writelines(lines)   # przekazujemy obiekt po którym można iterować
f.close()
# my_file.txt
# This is line 0This is line 1This is line 2...

f = open("my_file.txt", "r")
contents = f.readlines()  # zwróci listę
print(type(contents))
print(contents)
f.close()
# my_file.txt
# <class 'list'>
# ['This is line 0This is line 1This is line 2This is line 3...']


# -- 4 --
lines = [f"This is line {i}\n" for i in range(10)]
print(lines)
# >>> ['This is line 0\n', 'This is line 1\n', 'This is line 2\n', ...]

f = open("my_file.txt", "w")
f.writelines(lines)  # przekazujemy obiekt po którym można iterować
f.close()
# my_file.txt
# This is line 0
# This is line 1
# This is line 2

f = open("my_file.txt", "r")
contents = f.readlines()  # zwróci listę
print(type(contents))
print(contents)
f.close()
# >>> <class 'list'>
# >>> ['This is line 0\n', 'This is line 1\n', 'This is line 2\n', ...]

