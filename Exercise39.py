n=int(input('Sound level in decibels: '))
a='Quiet room'
b='Alarm clock'
c='Gas lawnmower'
d ='Jackhammer'
if n<40:
    print('Value smaller than the quietset noise in the table')
elif n==40:
    print('The noise is',a)
elif n<70:
    print('The noise is between',a,'and',b)
elif n==70:
     print('The noise is',b)
elif n<106:
    print('The noise is between',b,'and',c)   
elif n==106:
     print('The noise is',c)
elif n<130:
    print('The noise is between',c,'and',d) 
elif n==130:
     print('The noise is',d) 
else:
    print('Value larger than the loudest noise in the table')