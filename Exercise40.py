print('Enter the lengths of 3 sides of a triangle:')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if (a+b>c) and (a+c>b) and (b+c>a) and (a and b and c > 0):
    if a==b or a==c or b==c :
        tg='Isosceles triangle'
    elif (a==b==c):
        tg='Equilateral triangle'
    else:
        tg='Scalene triangle'
else: tg='ERROR'
print(tg)