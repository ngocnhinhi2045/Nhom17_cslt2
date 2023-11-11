a=int(input('Number of sides: '))
if 3<=a<=10:
    if a==3:
        z='Triangle'
    elif a==4:
        z='Quadrangle'
    elif a==5:
        z='Pentagon'
    elif a==6:
        z='Hexagon'
    elif a==7:
        z='Heptagon'
    elif a==8:
        z='Octagon'
    elif a==9:
        z='Nonagon'
    elif a==10:
        z='Decagon'
else:
    z='Error'
print(z)
