# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 14:10:35 2025

@author: VIK
"""

article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British comedy troupe formed in 1969 consisting of Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones and Michael Palin. The group came to prominence for the sketch comedy series Monty Python\'s Flying Circus, which aired on the BBC from 1969 to 1974. Their work then developed into a larger collection that included live shows, films, albums, books, and musicals; their influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Their sketch show has been called "an important moment in the evolution of television comedy".[7]

Monty Python's Flying Circus was loosely structured as a sketch show, but its innovative stream-of-consciousness approach and Gilliam\'s animation skills pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy unit, the Pythons had creative control that allowed them to experiment with form and content, discarding rules of television comedy.[10] They followed their television work by making the films Monty Python and the Holy Grail (1975), Life of Brian (1979), and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while it has coloured the work of the early editions of Saturday Night Live through to absurdist trends in television comedy.

At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution to Cinema. In 1998, they were awarded the AFI Star Award by the American Film Institute. Holy Grail and Life of Brian are frequently ranked on lists of the greatest comedy films. A 2005 poll asked more than 300 comedians, comedy writers, producers, and directors to name the greatest comedians of all time, and half of Monty Python's members made the top 50.[11][12]'''

print(article.upper())

print(article.lower().replace('monty', 'flying'))

print(article.split(' '))

print('Word \"Python\" appears ', article.lower().count('python'), 'times.')

print('to print the \\ you need to put \\ twice in your text like this: \\\\' )

print('The best hits of \'80s!!!')

print("The best hits of '80s!!!")

#######################################

amountPLN = 234

print('cur','\t','exchange','\t','amount')
print('USD','\t',3.65,'\t',amountPLN/3.65)
print('EUR','\t',4.23,'\t',amountPLN/4.23)


#######################################

ValueAsText = '123.45'
factor = 1.23

print('value is', ValueAsText, 'factor is', factor, 'value*factor=', float(ValueAsText)*factor)