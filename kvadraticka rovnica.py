import math
a=int(input('Zadaj číslo pre a: '))
b=int(input('Zadaj číslo pre b: '))
c=int(input('Zadaj číslo pre c: '))
#d => diskriminant
d= b*b-4*a*c
if d < 0:
    print('Rovnica nemá žiadne riešenie')
else:
    x1=((-b)+sqrt(d)/(2*a))
    x2=((-b)-sqrt(d)/(2*a))

    