n=str(input('Name of the month: '))
if n in ("April", "June", "September", "November"):
    days='30 days'
    print(n,'has', days)
elif n=='February':
    days='28 or 29 days'
    print(n,'has', days)
elif n in ("January", "March", "May", "July","August","October","December"): 
    days= '31 days'
    print(n,'has', days)
else: print('ERROR')
    