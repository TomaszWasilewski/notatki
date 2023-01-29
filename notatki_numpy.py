# Sample data randomly at fixed probabilities
np.random.choice(a = ["asian","black","hispanic","other","white"],
                 p = [0.05, 0.15 ,0.25, 0.05, 0.5],
                 size = 1000)[:10]
# >>> array(['white', 'hispanic', 'hispanic', 'white', 'asian', 'black',
# >>>       'white', 'white', 'white', 'hispanic'], dtype='<U8')                 
------------------------------------------------------

# numpy.outer(a, b, out=None)   -   computes the outer product of two vectors.
np.outer([1, 2, 3], [4, 5, 6])
# >>>array([[ 4,  5,  6],
# >>>       [ 8, 10, 12],
# >>>       [12, 15, 18]])
------------------------------------------------------

# Dodanie komórek będących sumą wartości z wiersza i komórek będących sumą wartości z kolumny
# i komórki będącej sumą wszystkich komórek.
data = np.array([[6400,1150],[5450,1300],[18200,3510],[8140,1668]])
data1 = np.concatenate((data,data.sum(axis=1)[:,None]),axis=1)
data1 = np.concatenate((data1,data1.sum(axis=0)[:,None].T),axis=0)       # .T - transpozycja
data1
# >>> array([[ 6400,  1150,  7550],
# >>>        [ 5450,  1300,  6750],
# >>>        [18200,  3510, 21710],
# >>>        [ 8140,  1668,  9808],
# >>>        [38190,  7628, 45818]])
-----------------------------------------------------

np.nansum() :
Kurs Data Science/zjazd_7/dzien_1/Z7_D1/Dane wielowymiarowe/Dane wielowymiarowe.ipynb
-----------------------------------------------------

np.all() :
Kurs Data Science/zjazd_7/dzien_1/Z7_D1/Dane wielowymiarowe/Dane wielowymiarowe.ipynb
-----------------------------------------------------

np.random.seed(100)
m = np.random.randint(1,11,size=(6, 10))
m
# >>> array([[ 9,  9,  4,  8,  8,  1,  5,  3,  6,  3],
# >>>        [ 3,  3,  2,  1,  9,  5,  1, 10,  7,  3],
# >>>        [ 5,  2,  6,  4,  5,  5,  4,  8,  2,  2],
# >>>        [ 8,  8,  1,  3, 10, 10,  4,  3,  6,  9],
# >>>        [ 2,  1,  8,  7,  3,  1,  9,  3,  6,  2],
# >>>        [ 9,  2,  6,  5,  3,  9,  4,  6,  1, 10]])

np.unique(m, return_counts=True)
# >>> (array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]),   w całej macierzy jedynka wyst. 7 razy, dwójka 7 razy itd.
# >>>  array([ 7,  7, 10,  5,  6,  6,  2,  6,  7,  4]))

-----------------------------------------------------

m = np.array([1,2,3,np.nan,5,6,7,np.nan])
# array([ 1.,  2.,  3., nan,  5.,  6.,  7., nan])
m[~np.isnan(m)]
# >>> array([1., 2., 3., 5., 6., 7.])

-----------------------------------------------------

# Znajdź indeksy duplikatów, oznacz je jako True. Pierwsze wystąpienie danej wartości powinno być oznaczone jako False
a = np.array([0, 0, 3, 0, 2, 4, 2, 2, 2, 2])
np.array([True if a[i] in a[:i] else False for i in range(np.size(a))])
# >>> array([False,  True, False,  True, False, False,  True,  True,  True, True])

-----------------------------------------------------

# Policz ile elementów w macierzy jest niezerowych
x = np.array([[0,1,7,0,22],
              [3,0,0,2,19]])
np.where(x != 0, 1, 0).sum()
# >>> 6



