a=int(input('Human years: '))
if a<0:
    print('Error')
elif a<=2:
    b=10.5*a
    print('Dog years:',b)
elif a>2:
    b=10.5*2 + 4*(a-2)
    print('Dog years:',b)