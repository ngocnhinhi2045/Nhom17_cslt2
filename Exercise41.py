n=str(input('Name of a note (C,D,E...): '))
m=int(input('The octave (1,2,3...): '))
C4=261.63
D4= 293.66
E4= 329.63 
F4= 349.23 
G4= 392.00 
A4=  440.00 
B4= 493.88
if n=='C':
    frequency=C4 / 2**(4-m)
elif n=='D':
    frequency=D4 / 2**(4-m)
elif n=='E':
    frequency=E4 / 2**(4-m)
elif n=='F':
    frequency=F4 / 2**(4-m)
elif n=='G':
    frequency=G4 / 2**(4-m)
elif n=='A':
    frequency=A4 / 2**(4-m)
elif n=='B':
    frequency=B4 / 2**(4-m)
print('Frequency of ',n,m, ' is: ', round(frequency,2),'Hz', sep="")