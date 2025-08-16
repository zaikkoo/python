num = int(input('Digite um número: '))
print(f'Analisando o número {num}.')

uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10

print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}')