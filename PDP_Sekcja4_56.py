# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 14:27:35 2025

@author: VIK
"""

'''
Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50.
Całość pomnóż przez 20, a następnie dodaj 1017. Odejmij od tego swój rok urodzenia.
Wyszła 4cyfrowa liczba. Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.
'''

numerButa = 44
x = ( numerButa * 5 + 50 ) * 20 + 1025 - 1991
print('Shoe size is', x //100,'.' )
print('Age is', x %100, 'years.')

'''
Pomyśl liczbe nieujemną całkowitą. Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę.
Powinno wyjść 5 - zawsze.
'''
y = 121
number = (y * 2 + 10 ) / 2 - 121
print('This should be 5:', number)

z = 2 + 2 * 2
print('2 + 2 * 2 =', z)

v = 7 + 7 / 7 + 7 * 7 - 7
print('7 + 7 / 7 + 7 * 7 - 7 =', v)



# Student1: obecnosc 0.85, średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie.

presence = 0.85
note = 3.5
finalWork = True

print('You need to be present and have good grades or create final work. Did you passed?:',(presence >= 0.8 and note >= 3.5) or finalWork)

# Student2
presence = 0.4
note = 2.5
finalWorkOK = True
print('you need to be present and have good notes or do the final work. Did you passed?:',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work. Did you passed?:',presence >=0.8 and note >=3 and finalWorkOK)
