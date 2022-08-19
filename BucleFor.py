import numpy as np

a = np.array([13,55,28,67,96,35])

b= len(a)
rr = range(b)

"""
for i in rr:
    if a[i]==66:
        print('Hola bro')

    elif a[i] ==77:
        print('Lacin')

    elif a[i] <=28:
        print('2° Lacin')

    else:                   #Todo lo que la funcion no cumple
        print('bye')
"""

b= np.array(['Mk', 'Mn', 'Ms', 'Md'])
l2=len(b)
r2=range(l2)

for i in r2:
    if b[i] =='Mk':
        print('Holi')

    elif b[i] >= 'Mn':
        print('Un Lacin')

    else:
        print('Error')