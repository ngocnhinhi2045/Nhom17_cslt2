day=int(input('Day:'))
month=int(input('Month:'))
if day==1 and month==1:
    print("New year's day")
elif day==1 and month==7:
    print('Canada day')
elif day==25 and month==12:
    print('Christmas day')   
else:
    print('Do not correspond to a fixed-date holiday.') 
