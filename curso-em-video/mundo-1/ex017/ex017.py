import math

catoposto = float(input('Comprimento do cateto oposto: '))
catadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catoposto, catadjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f}.')