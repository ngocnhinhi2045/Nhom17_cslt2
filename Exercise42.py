n = float(input('Enter the frequency: '))
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
if (C4 - 1) <= n <= (C4 + 1):
    print('The name of the note is C4.')
elif (D4 - 1) <= n <= (D4 + 1):
    print('The name of the note is D4.')
elif (E4 - 1) <= n <= (E4 + 1):
    print('The name of the note is E4.')
elif (F4 - 1) <= n <= (F4 + 1):
    print('The name of the note is F4.')
elif (G4 - 1) <= n <= (G4 + 1):
    print('The name of the note is G4.')
elif (A4 - 1) <= n <= (A4 + 1):
    print('The name of the note ise A4.')
elif (B4 - 1) <= n <= (B4 + 1):
    print('The name of the note is B4.')
else:
    print('The frequency does not correspond to a known note.')
