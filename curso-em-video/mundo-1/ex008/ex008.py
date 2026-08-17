''' Exercício 008 - Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros. '''

distancia = float(input('Uma distância em metros: '))

km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print(f'A medida de {distancia:.1f} corresponde a: ')

print(f'{km} km')
print(f'{hm} hm')
print(f'{dam} dam')
print(f'{dm:.0f} dm')
print(f'{cm:.0f} cm')
print(f'{mm:.0f} mm')