# Celcius to Fehrenhrit
print('Enter 5 Celcius Values:')
vals = [int(input()) for x in range(5)]
Fer =[]
for i in vals:
    Fer.append(i*9/5+32)
print('Fehrenheit values are')
print(Fer)
